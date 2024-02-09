from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.project_request_itemput_request_schema import ProjectRequestItemputRequestSchema
from ...models.project_request_itemput_response_schema import ProjectRequestItemputResponseSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: int,
    json_body: ProjectRequestItemputRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Dict[str, Any]:
    url = "{}/projectrequests/{id}".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "offset": offset,
        "limit": limit,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ProjectRequestItemputResponseSchema]:
    if response.status_code == 200:
        response_200 = ProjectRequestItemputResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ProjectRequestItemputResponseSchema]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: int,
    json_body: ProjectRequestItemputRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Response[ProjectRequestItemputResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
        offset=offset,
        limit=limit,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: int,
    json_body: ProjectRequestItemputRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Optional[ProjectRequestItemputResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
        id=id,
        json_body=json_body,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: int,
    json_body: ProjectRequestItemputRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Response[ProjectRequestItemputResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
        offset=offset,
        limit=limit,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: int,
    json_body: ProjectRequestItemputRequestSchema,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 300,
) -> Optional[ProjectRequestItemputResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            json_body=json_body,
            offset=offset,
            limit=limit,
        )
    ).parsed
