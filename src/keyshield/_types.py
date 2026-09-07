from contextlib import AbstractAsyncContextManager
from typing import TYPE_CHECKING, Callable, Awaitable

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from keyshield.domain.entities import ApiKey
from keyshield.services.base import AbstractApiKeyService

if TYPE_CHECKING:
    # Only the FastAPI connector (api.py) actually needs fastapi at runtime. This
    # module is also imported by the SQLAlchemy/Litestar CLI, so importing fastapi
    # here would force it as a hard dependency. Keep it type-only.
    from fastapi.security import HTTPAuthorizationCredentials


AsyncSessionMaker = async_sessionmaker[AsyncSession]
"""Type alias for an "async_sessionmaker" instance of SQLAlchemy."""

SecurityHTTPBearer = Callable[["HTTPAuthorizationCredentials"], Awaitable[ApiKey]]
"""Type alias for a security dependency callable using HTTP Bearer scheme."""

SecurityAPIKeyHeader = Callable[[str], Awaitable[ApiKey]]
"""Type alias for a security dependency callable using API Key Header scheme."""

ServiceFactory = Callable[[], AbstractAsyncContextManager[AbstractApiKeyService]]
"""Callable returning an async context manager that yields an API key service instance."""
