# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, List, Optional, TypeVar
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import _deserialize
from .._serialization import Serializer
from .._vendor import BatchClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_batch_list_pools_request(
    *,
    _filter: Optional[str] = None,
    _select: Optional[List[str]] = None,
    _expand: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/pools"

    # Construct parameters
    if _filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", _filter, "str")
    if _select is not None:
        _params["$select"] = _SERIALIZER.query("select", _select, "[str]", div=",")
    if _expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", _expand, "[str]", div=",")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_batch_list_pools2_request(
    *,
    _filter: Optional[str] = None,
    _select: Optional[List[str]] = None,
    _expand: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/pools2"

    # Construct parameters
    if _filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", _filter, "str")
    if _select is not None:
        _params["$select"] = _SERIALIZER.query("select", _select, "[str]", div=",")
    if _expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", _expand, "[str]", div=",")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_batch_list_pools3_request(
    *,
    _filter: Optional[str] = None,
    _select: Optional[List[str]] = None,
    _expand: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-05-01.17.0"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/pools3"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if _filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", _filter, "str")
    if _select is not None:
        _params["$select"] = _SERIALIZER.query("select", _select, "[str]", div=",")
    if _expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", _expand, "[str]", div=",")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class BatchClientOperationsMixin(BatchClientMixinABC):
    @distributed_trace
    def list_pools(
        self,
        *,
        _filter: Optional[str] = None,
        _select: Optional[List[str]] = None,
        _expand: Optional[List[str]] = None,
        **kwargs: Any
    ) -> Iterable["_models.BatchPool"]:
        """Lists all of the Pools in the specified Account.

        :keyword _filter: An OData $filter clause. For more information on constructing this filter,
         see
         https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-pools.
         Default value is None.
        :paramtype _filter: str
        :keyword _select: An OData $select clause. Default value is None.
        :paramtype _select: list[str]
        :keyword _expand: An OData $expand clause. Default value is None.
        :paramtype _expand: list[str]
        :return: An iterator like instance of BatchPool
        :rtype: ~azure.core.paging.ItemPaged[~azure.batch.models.BatchPool]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.BatchPool]] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_batch_list_pools_request(
                    _filter=_filter,
                    _select=_select,
                    _expand=_expand,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request.url = self._client.format_url(request.url)

            return request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.BatchPool], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("odata.nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                if _stream:
                    response.read()  # Load the body in memory and close the socket
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _deserialize(_models.BatchError, response.json())
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def list_pools2(
        self,
        *,
        _filter: Optional[str] = None,
        _select: Optional[List[str]] = None,
        _expand: Optional[List[str]] = None,
        **kwargs: Any
    ) -> Iterable["_models.BatchPool"]:
        """Lists all of the Pools in the specified Account.

        :keyword _filter: An OData $filter clause. For more information on constructing this filter,
         see
         https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-pools.
         Default value is None.
        :paramtype _filter: str
        :keyword _select: An OData $select clause. Default value is None.
        :paramtype _select: list[str]
        :keyword _expand: An OData $expand clause. Default value is None.
        :paramtype _expand: list[str]
        :return: An iterator like instance of BatchPool
        :rtype: ~azure.core.paging.ItemPaged[~azure.batch.models.BatchPool]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.BatchPool]] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_batch_list_pools2_request(
                    _filter=_filter,
                    _select=_select,
                    _expand=_expand,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request.url = self._client.format_url(request.url)

            return request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.BatchPool], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("odata.nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                if _stream:
                    response.read()  # Load the body in memory and close the socket
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _deserialize(_models.BatchError, response.json())
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def list_pools3(
        self,
        *,
        _filter: Optional[str] = None,
        _select: Optional[List[str]] = None,
        _expand: Optional[List[str]] = None,
        **kwargs: Any
    ) -> Iterable["_models.BatchPool"]:
        """Lists all of the Pools in the specified Account.

        :keyword _filter: An OData $filter clause. For more information on constructing this filter,
         see
         https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-pools.
         Default value is None.
        :paramtype _filter: str
        :keyword _select: An OData $select clause. Default value is None.
        :paramtype _select: list[str]
        :keyword _expand: An OData $expand clause. Default value is None.
        :paramtype _expand: list[str]
        :return: An iterator like instance of BatchPool
        :rtype: ~azure.core.paging.ItemPaged[~azure.batch.models.BatchPool]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.BatchPool]] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_batch_list_pools3_request(
                    _filter=_filter,
                    _select=_select,
                    _expand=_expand,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request.url = self._client.format_url(request.url)

            return request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.BatchPool], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("odata.nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                if _stream:
                    response.read()  # Load the body in memory and close the socket
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _deserialize(_models.BatchError, response.json())
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)