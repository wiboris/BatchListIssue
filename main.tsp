import "@typespec/rest";
import "@typespec/versioning";
import "@typespec/http";
import "@azure-tools/typespec-azure-core";
import "@typespec/rest";
import "@azure-tools/typespec-client-generator-core";

using TypeSpec.Reflection;
using TypeSpec.Http;
using TypeSpec.Rest;
using TypeSpec.Versioning;
using Azure.Core;
using Azure.Core.Traits;
using Azure.ClientGenerator.Core;

@service({
  title: "Azure Batch",
})
@versioned(Azure.Batch.Versions)
@doc("Azure Batch provides Cloud-scale job scheduling and compute management.")

namespace Azure.Batch;

@doc("The Azure Batch service version.")
enum Versions {
   @doc("API Version 2023-05-01.17.0")
   @useDependency(Azure.Core.Versions.v1_0_Preview_2)
  `2023-05-01.17.0`,
}


interface Pools {

  @doc("Lists all of the Pools in the specified Account.")
  @route("/pools")
  @get
  op listPools(
    ...BatchRequestHeaders
  ): BatchResponseHeaders & BatchPoolListResult | BatchError;


  @doc("Lists all of the Pools in the specified Account.")
  @route("/pools2")
  @get
  op listPools2(
    ...BatchRequestHeaders
  ): BatchPoolListResult | BatchError;


  @doc("Lists all of the Pools in the specified Account.")
  @route("/pools3")
  @get
  listPools3 is RpcOperation<
  BatchRequestHeaders,
  BatchResponseHeaders & BatchPoolListResult,
  {},
  BatchError
>;
}



#suppress "@azure-tools/typespec-azure-core/casing-style" "The names of Model types must use camelCase"
@doc("Client related response header values")
model BatchRequestHeaders {
    @doc("""
    An OData $filter clause. For more information on constructing this filter, see
    https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-pools.
    """)
        @query
        $filter?: string;
    
        @doc("An OData $select clause.")
        @query({ format: "csv" })
        $select?: string[];
    
        @doc("An OData $expand clause.")
        @query({ format: "csv" })
        $expand?: string[];
}


#suppress "@azure-tools/typespec-azure-core/casing-style" "The names of Model types must use camelCase"
@doc("Client related response header values")
model BatchResponseHeaders {
  @doc("The client-request-id provided by the client during the request. This will be returned only if the return-client-request-id parameter was set to true.")
  @header
  `client-request-id`?: string;

  @doc("A unique identifier for the request that was made to the Batch service. If a request is consistently failing and you have verified that the request is properly formulated, you may use this value to report the error to Microsoft. In your report, include the value of this request ID, the approximate time that the request was made, the Batch Account against which the request was made, and the region that Account resides in.")
  @header
  `request-id`?: string;

  @doc("The ETag HTTP response header. This is an opaque string. You can use it to detect whether the resource has changed between requests. In particular, you can pass the ETag to one of the If-Modified-Since, If-Unmodified-Since, If-Match or If-None-Match headers.")
  @header
  @projectedName("python", "etag")
  ETag?: string;

  @doc("The time at which the resource was last modified.")
  @header
  @encode(DateTimeKnownEncoding.rfc7231)
  `Last-Modified`?: utcDateTime;
}



@doc("The result of listing the Pools in an Account.")
@pagedResult
model BatchPoolListResult {
  @doc("The list of Pools.")
  @items
  value?: BatchPool[];

  #suppress "@azure-tools/typespec-azure-core/casing-style" "The names of Property types must use camelCase"
  @doc("The URL to get the next set of results.")
  @nextLink
  `odata.nextLink`?: string;
}


@doc("A Pool in the Azure Batch service.")
model BatchPool {
  @doc("A string that uniquely identifies the Pool within the Account. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case).")
  @visibility("read")
  id?: string;

  @doc("The display name for the Pool. The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.")
  @visibility("read")
  displayName?: string;

  @doc("The URL of the Pool.")
  @visibility("read")
  url?: string;
}



@doc("An error response received from the Azure Batch service.")
@error
model BatchError {
  @doc("An identifier for the error. Codes are invariant and are intended to be consumed programmatically.")
  code: string;

  @doc("A message describing the error, intended to be suitable for display in a user interface.")
  message?: ErrorMessage;

  @doc("A collection of key-value pairs containing additional details about the error.")
  values?: BatchErrorDetail[];
}

@doc("An error message received in an Azure Batch error response.")
model ErrorMessage {
  @doc("The language code of the error message.")
  lang?: string;

  @doc("The text of the message.")
  value?: string;
}

@doc("An item of additional information included in an Azure Batch error response.")
model BatchErrorDetail {
  @doc("An identifier specifying the meaning of the Value property.")
  key?: string;

  @doc("The additional information included with the error response.")
  value?: string;
}