import os
import taikunpycore
from taikunpycore.rest import ApiException
from taikunpycore import Configuration, ApiClient
from taikunpycore.api.auth_management_api import AuthManagementApi
from taikunpycore.models import LoginCommand

class TaikunClient:
    def __init__(self, api_host=None):
        """Initialize the Taikun API Client and authenticate."""
        if api_host is None:
            self.api_host = 'https://' + os.getenv("TAIKUN_API_HOST", "api.taikun.cloud")
        else:
            self.api_host = 'https://' + api_host
        # self.api_host = api_host or os.getenv("TAIKUN_API_HOST", "api.taikun.cloud")
        self.token = None
        self.refresh_token = None
        self.configuration = Configuration()
        self.configuration.host = self.api_host
        self.api_client = ApiClient(self.configuration)
        self._authenticate()

    def _authenticate(self):
        """Authenticate the client using environment credentials."""
        email = os.getenv("TAIKUN_EMAIL")
        password = os.getenv("TAIKUN_PASSWORD")
        auth_api = AuthManagementApi(self.api_client)

        if not email or not password:
            raise ValueError("Email and password must be provided for authentication.")

        try:
            response = auth_api.auth_login(LoginCommand(email=email, password=password))
            self.token = response.token
            self.refresh_token = response.refresh_token

            # Set authentication headers
            self.configuration.api_key["Bearer"] = self.token
            self.configuration.api_key_prefix["Bearer"] = "Bearer"

            # Reinitialize client with new token
            self.api_client = ApiClient(self.configuration)
            # print("Authenticated successfully!")

        except ApiException as e:
            print(f"Authentication failed: {e}")


