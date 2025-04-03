import os
import threading
from taikunpycore import Configuration, ApiClient
from taikunpycore.api import AuthManagementApi
from taikunpycore.models import LoginCommand
from taikunpycore.rest import ApiException


class TaikunClient:
    def __init__(self, api_host=None, auto_refresh_minutes=5):  # Default refresh to 10 minutes
        """Initialize the Taikun API Client and authenticate."""

        # Store how often to auto-refresh the token (in minutes)
        self._refresh_timer = None
        if auto_refresh_minutes is not None:
            self.auto_refresh_minutes = auto_refresh_minutes

        # Determine the API host from argument or environment variable
        if api_host is None:
            self.api_host = 'https://' + os.getenv("TAIKUN_API_HOST", "api.taikun.cloud")
        else:
            self.api_host = 'https://' + api_host

        # Token values will be set after authentication
        self.token = None
        self.refresh_token = None

        # Create initial API client configuration
        self.configuration = Configuration()
        self.configuration.host = self.api_host
        self.api_client = ApiClient(self.configuration)

        # Perform initial authentication
        self._authenticate()

        # Start background auto-refresh if enabled
        if self.auto_refresh_minutes:
            self._start_auto_refresh()

    def _authenticate(self):
        """Authenticate the client using environment credentials."""
        auth_mode = os.getenv("TAIKUN_AUTH_MODE", "default").lower()
        email = os.getenv("TAIKUN_EMAIL")
        password = os.getenv("TAIKUN_PASSWORD")
        access_token = os.getenv("TAIKUN_ACCESS_KEY")
        secret_token = os.getenv("TAIKUN_SECRET_KEY")

        # Create the API interface for authentication
        auth_api = AuthManagementApi(self.api_client)

        try:
            # Email/password auth (default mode)
            if email and password and (auth_mode == "default" or auth_mode == ''):
                response = auth_api.auth_login(LoginCommand(email=email, password=password))

            # Token-based auth
            elif access_token and secret_token and auth_mode == "token":
                response = auth_api.auth_login(LoginCommand(accessKey=access_token, secretKey=secret_token, mode="token"))

            # No valid credentials
            else:
                raise ValueError("Valid authentication credentials must be provided.")

            # Store tokens from the response
            self.token = response.token
            self.refresh_token = response.refresh_token

            # Apply token to the configuration for API authentication
            self.configuration.api_key["Bearer"] = self.token
            self.configuration.api_key_prefix["Bearer"] = "Bearer"

            # Reinitialize the API client with updated headers
            self.api_client = ApiClient(self.configuration)

            print("[TaikunClient] Authentication successful.")

        except ApiException as e:
            print(f"[TaikunClient] Authentication failed: {e}")

    def _start_auto_refresh(self):
        """Start the background token refresh loop."""
        def refresh_loop():
            print("[TaikunClient] Auto-refreshing token...")
            self._authenticate()  # Refresh the token
            # Schedule next refresh
            self._refresh_timer = threading.Timer(self.auto_refresh_minutes * 60, refresh_loop)
            self._refresh_timer.daemon = True  # Won't block program from exiting
            self._refresh_timer.start()

        refresh_loop()  # Start the first refresh immediately

    def stop_auto_refresh(self):
        """Stop the auto-refresh background task."""
        if self._refresh_timer:
            self._refresh_timer.cancel()
            print("[TaikunClient] Auto-refresh stopped.")

    @property
    def connection_info(self):
        """Expose connection-related info (for debugging/logging)."""
        return {
            "api_host": self.api_host,
            "token": self.token,
            "refresh_token": self.refresh_token,
            "configuration_host": self.configuration.host,
        }
