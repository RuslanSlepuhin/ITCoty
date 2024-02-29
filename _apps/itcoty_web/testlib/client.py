from dataclasses import dataclass

import orjson
import requests
from pydantic import BaseModel, Extra


class MyModel(BaseModel):
    class Meta:
        extra = Extra.forbid
        json_dumps = orjson.dumps
        json_loads = orjson.loads
        orm_mode = True
        validate_assignment = True


class TokenPairResponse(MyModel):
    access: str
    refresh: str


class VerifyTokenResponse(MyModel):
    detail: str = "OK"


class Authority(MyModel):
    password: str
    username: str


class RegisterResponse(MyModel):
    message: str
    user: Authority


class ActivateResponse(MyModel):
    message: str


class InitiatePassowrdResetResponse(MyModel):
    message: str
    pass_secret_key: str
    user: Authority


class ConfirmPasswordResetResponse(MyModel):
    message: str
    pass_secret_key: str


class ResetPasswordResponse(MyModel):
    message: str


class ResendCodeResponse(MyModel):
    message: str


class DeleteUserResponse(MyModel):
    message: str


@dataclass
class Client:
    host: str
    session: requests.Session

    class ApiError(RuntimeError):
        def __init__(
            self,
            *args: tuple,
            message: str,
            http_code: int,
        ):
            super().__init__(*args)
            self.message = message
            self.http_code = http_code

        def __str__(self) -> str:
            return f"message:{self.message}, http_code:{self.http_code}"

    def register(
        self,
        *,
        password: str,
        username: str,
    ) -> RegisterResponse:
        response = self.session.post(
            f"{self.host}/api/signup/",
            data=orjson.dumps(
                {
                    "password": password,
                    "password2": password,
                    "username": username,
                }
            ),
        )
        assert response.ok, response.text
        payload = RegisterResponse.parse_raw(response.text)
        return payload

    def activate(
        self,
        *,
        otp_code: str,
        username: str,
    ) -> ActivateResponse:
        response = self.session.post(
            f"{self.host}/api/signup_complete/",
            data=orjson.dumps(
                {
                    "otp_code": otp_code,
                    "username": username,
                }
            ),
        )
        assert response.ok, response.text
        payload = ActivateResponse.parse_raw(response.text)
        return payload

    def authenticate(
        self,
        *,
        password: str,
        username: str,
    ) -> TokenPairResponse:
        response = self.session.post(
            f"{self.host}/api/login/",
            data={
                "password": password,
                "username": username,
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )
        assert response.ok, response.text
        payload = TokenPairResponse.parse_raw(response.text)
        return payload
