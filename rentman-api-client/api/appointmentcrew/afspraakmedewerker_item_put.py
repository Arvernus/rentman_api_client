from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.afspraakmedewerker_itemput_request_schema import AfspraakmedewerkerItemputRequestSchema
from ...models.afspraakmedewerker_itemput_response_schema import AfspraakmedewerkerItemputResponseSchema
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    id: int,
    json_body: AfspraakmedewerkerItemputRequestSchema,
) -> Dict[str, Any]:
    url = "{}/appointmentcrew/{id}".format(client.base_url, id=id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AfspraakmedewerkerItemputResponseSchema]:
    if response.status_code == 200:
        response_200 = AfspraakmedewerkerItemputResponseSchema.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AfspraakmedewerkerItemputResponseSchema]:
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
    json_body: AfspraakmedewerkerItemputRequestSchema,
) -> Response[AfspraakmedewerkerItemputResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: int,
    json_body: AfspraakmedewerkerItemputRequestSchema,
) -> Optional[AfspraakmedewerkerItemputResponseSchema]:
    """ """

    return sync_detailed(
        client=client,
        id=id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: int,
    json_body: AfspraakmedewerkerItemputRequestSchema,
) -> Response[AfspraakmedewerkerItemputResponseSchema]:
    kwargs = _get_kwargs(
        client=client,
        id=id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: int,
    json_body: AfspraakmedewerkerItemputRequestSchema,
) -> Optional[AfspraakmedewerkerItemputResponseSchema]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            json_body=json_body,
        )
    ).parsed
