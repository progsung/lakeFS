"""
    lakeFS API

    lakeFS HTTP API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: services@treeverse.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from lakefs_client.api_client import ApiClient, Endpoint as _Endpoint
from lakefs_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from lakefs_client.model.error import Error
from lakefs_client.model.garbage_collection_prepare_request import GarbageCollectionPrepareRequest
from lakefs_client.model.garbage_collection_prepare_response import GarbageCollectionPrepareResponse
from lakefs_client.model.garbage_collection_rules import GarbageCollectionRules
from lakefs_client.model.prepare_gc_uncommitted_request import PrepareGCUncommittedRequest
from lakefs_client.model.prepare_gc_uncommitted_response import PrepareGCUncommittedResponse


class RetentionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_garbage_collection_rules_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth'
                ],
                'endpoint_path': '/repositories/{repository}/gc/rules',
                'operation_id': 'delete_garbage_collection_rules',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                ],
                'required': [
                    'repository',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                },
                'attribute_map': {
                    'repository': 'repository',
                },
                'location_map': {
                    'repository': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_garbage_collection_rules_endpoint = _Endpoint(
            settings={
                'response_type': (GarbageCollectionRules,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth'
                ],
                'endpoint_path': '/repositories/{repository}/gc/rules',
                'operation_id': 'get_garbage_collection_rules',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                ],
                'required': [
                    'repository',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                },
                'attribute_map': {
                    'repository': 'repository',
                },
                'location_map': {
                    'repository': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.prepare_garbage_collection_commits_endpoint = _Endpoint(
            settings={
                'response_type': (GarbageCollectionPrepareResponse,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth'
                ],
                'endpoint_path': '/repositories/{repository}/gc/prepare_commits',
                'operation_id': 'prepare_garbage_collection_commits',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'garbage_collection_prepare_request',
                ],
                'required': [
                    'repository',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'garbage_collection_prepare_request':
                        (GarbageCollectionPrepareRequest,),
                },
                'attribute_map': {
                    'repository': 'repository',
                },
                'location_map': {
                    'repository': 'path',
                    'garbage_collection_prepare_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.prepare_garbage_collection_uncommitted_endpoint = _Endpoint(
            settings={
                'response_type': (PrepareGCUncommittedResponse,),
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth'
                ],
                'endpoint_path': '/repositories/{repository}/gc/prepare_uncommited',
                'operation_id': 'prepare_garbage_collection_uncommitted',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'prepare_gc_uncommitted_request',
                ],
                'required': [
                    'repository',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'prepare_gc_uncommitted_request':
                        (PrepareGCUncommittedRequest,),
                },
                'attribute_map': {
                    'repository': 'repository',
                },
                'location_map': {
                    'repository': 'path',
                    'prepare_gc_uncommitted_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.set_garbage_collection_rules_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'basic_auth',
                    'cookie_auth',
                    'jwt_token',
                    'oidc_auth'
                ],
                'endpoint_path': '/repositories/{repository}/gc/rules',
                'operation_id': 'set_garbage_collection_rules',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'repository',
                    'garbage_collection_rules',
                ],
                'required': [
                    'repository',
                    'garbage_collection_rules',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'repository':
                        (str,),
                    'garbage_collection_rules':
                        (GarbageCollectionRules,),
                },
                'attribute_map': {
                    'repository': 'repository',
                },
                'location_map': {
                    'repository': 'path',
                    'garbage_collection_rules': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def delete_garbage_collection_rules(
        self,
        repository,
        **kwargs
    ):
        """delete_garbage_collection_rules  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_garbage_collection_rules(repository, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        return self.delete_garbage_collection_rules_endpoint.call_with_http_info(**kwargs)

    def get_garbage_collection_rules(
        self,
        repository,
        **kwargs
    ):
        """get_garbage_collection_rules  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_garbage_collection_rules(repository, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GarbageCollectionRules
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        return self.get_garbage_collection_rules_endpoint.call_with_http_info(**kwargs)

    def prepare_garbage_collection_commits(
        self,
        repository,
        **kwargs
    ):
        """save lists of active and expired commits for garbage collection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.prepare_garbage_collection_commits(repository, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):

        Keyword Args:
            garbage_collection_prepare_request (GarbageCollectionPrepareRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            GarbageCollectionPrepareResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        return self.prepare_garbage_collection_commits_endpoint.call_with_http_info(**kwargs)

    def prepare_garbage_collection_uncommitted(
        self,
        repository,
        **kwargs
    ):
        """save repository uncommitted metadata for garbage collection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.prepare_garbage_collection_uncommitted(repository, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):

        Keyword Args:
            prepare_gc_uncommitted_request (PrepareGCUncommittedRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PrepareGCUncommittedResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        return self.prepare_garbage_collection_uncommitted_endpoint.call_with_http_info(**kwargs)

    def set_garbage_collection_rules(
        self,
        repository,
        garbage_collection_rules,
        **kwargs
    ):
        """set_garbage_collection_rules  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_garbage_collection_rules(repository, garbage_collection_rules, async_req=True)
        >>> result = thread.get()

        Args:
            repository (str):
            garbage_collection_rules (GarbageCollectionRules):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['repository'] = \
            repository
        kwargs['garbage_collection_rules'] = \
            garbage_collection_rules
        return self.set_garbage_collection_rules_endpoint.call_with_http_info(**kwargs)

