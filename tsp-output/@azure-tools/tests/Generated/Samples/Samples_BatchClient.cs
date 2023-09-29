// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

// <auto-generated/>

#nullable disable

using System;
using System.Text.Json;
using System.Threading.Tasks;
using Azure;
using Azure.Compute.Batch;
using Azure.Identity;
using NUnit.Framework;

namespace Azure.Compute.Batch.Samples
{
    public partial class Samples_BatchClient
    {
        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools_ShortVersion()
        {
            BatchClient client = new BatchClient();

            Response response = client.GetPools(null, null, null, null);

            JsonElement result = JsonDocument.Parse(response.ContentStream).RootElement;
            Console.WriteLine(result.ToString());
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools_ShortVersion_Async()
        {
            BatchClient client = new BatchClient();

            Response response = await client.GetPoolsAsync(null, null, null, null);

            JsonElement result = JsonDocument.Parse(response.ContentStream).RootElement;
            Console.WriteLine(result.ToString());
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools_ShortVersion_Convenience()
        {
            BatchClient client = new BatchClient();

            Response<BatchPoolListResult> response = client.GetPools();
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools_ShortVersion_Convenience_Async()
        {
            BatchClient client = new BatchClient();

            Response<BatchPoolListResult> response = await client.GetPoolsAsync();
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools_AllParameters()
        {
            BatchClient client = new BatchClient();

            Response response = client.GetPools("<$filter>", new string[] { "<$select>" }, new string[] { "<$expand>" }, null);

            JsonElement result = JsonDocument.Parse(response.ContentStream).RootElement;
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("id").ToString());
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("displayName").ToString());
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("url").ToString());
            Console.WriteLine(result.GetProperty("odata.nextLink").ToString());
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools_AllParameters_Async()
        {
            BatchClient client = new BatchClient();

            Response response = await client.GetPoolsAsync("<$filter>", new string[] { "<$select>" }, new string[] { "<$expand>" }, null);

            JsonElement result = JsonDocument.Parse(response.ContentStream).RootElement;
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("id").ToString());
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("displayName").ToString());
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("url").ToString());
            Console.WriteLine(result.GetProperty("odata.nextLink").ToString());
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools_AllParameters_Convenience()
        {
            BatchClient client = new BatchClient();

            Response<BatchPoolListResult> response = client.GetPools(filter: "<$filter>", select: new string[] { "<$select>" }, expand: new string[] { "<$expand>" });
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools_AllParameters_Convenience_Async()
        {
            BatchClient client = new BatchClient();

            Response<BatchPoolListResult> response = await client.GetPoolsAsync(filter: "<$filter>", select: new string[] { "<$select>" }, expand: new string[] { "<$expand>" });
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools3s_ShortVersion()
        {
            BatchClient client = new BatchClient();

            Response response = client.GetPools3s(null, null, null, null);

            JsonElement result = JsonDocument.Parse(response.ContentStream).RootElement;
            Console.WriteLine(result.ToString());
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools3s_ShortVersion_Async()
        {
            BatchClient client = new BatchClient();

            Response response = await client.GetPools3sAsync(null, null, null, null);

            JsonElement result = JsonDocument.Parse(response.ContentStream).RootElement;
            Console.WriteLine(result.ToString());
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools3s_ShortVersion_Convenience()
        {
            BatchClient client = new BatchClient();

            Response<BatchPoolListResult> response = client.GetPools3s();
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools3s_ShortVersion_Convenience_Async()
        {
            BatchClient client = new BatchClient();

            Response<BatchPoolListResult> response = await client.GetPools3sAsync();
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools3s_AllParameters()
        {
            BatchClient client = new BatchClient();

            Response response = client.GetPools3s("<$filter>", new string[] { "<$select>" }, new string[] { "<$expand>" }, null);

            JsonElement result = JsonDocument.Parse(response.ContentStream).RootElement;
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("id").ToString());
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("displayName").ToString());
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("url").ToString());
            Console.WriteLine(result.GetProperty("odata.nextLink").ToString());
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools3s_AllParameters_Async()
        {
            BatchClient client = new BatchClient();

            Response response = await client.GetPools3sAsync("<$filter>", new string[] { "<$select>" }, new string[] { "<$expand>" }, null);

            JsonElement result = JsonDocument.Parse(response.ContentStream).RootElement;
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("id").ToString());
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("displayName").ToString());
            Console.WriteLine(result.GetProperty("value")[0].GetProperty("url").ToString());
            Console.WriteLine(result.GetProperty("odata.nextLink").ToString());
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools3s_AllParameters_Convenience()
        {
            BatchClient client = new BatchClient();

            Response<BatchPoolListResult> response = client.GetPools3s(filter: "<$filter>", select: new string[] { "<$select>" }, expand: new string[] { "<$expand>" });
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools3s_AllParameters_Convenience_Async()
        {
            BatchClient client = new BatchClient();

            Response<BatchPoolListResult> response = await client.GetPools3sAsync(filter: "<$filter>", select: new string[] { "<$select>" }, expand: new string[] { "<$expand>" });
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools2s_ShortVersion()
        {
            BatchClient client = new BatchClient();

            foreach (BinaryData item in client.GetPools2s(null, null, null, null))
            {
                JsonElement result = JsonDocument.Parse(item.ToStream()).RootElement;
                Console.WriteLine(result.ToString());
            }
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools2s_ShortVersion_Async()
        {
            BatchClient client = new BatchClient();

            await foreach (BinaryData item in client.GetPools2sAsync(null, null, null, null))
            {
                JsonElement result = JsonDocument.Parse(item.ToStream()).RootElement;
                Console.WriteLine(result.ToString());
            }
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools2s_ShortVersion_Convenience()
        {
            BatchClient client = new BatchClient();

            foreach (BatchPool item in client.GetPools2s())
            {
            }
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools2s_ShortVersion_Convenience_Async()
        {
            BatchClient client = new BatchClient();

            await foreach (BatchPool item in client.GetPools2sAsync())
            {
            }
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools2s_AllParameters()
        {
            BatchClient client = new BatchClient();

            foreach (BinaryData item in client.GetPools2s("<$filter>", new string[] { "<$select>" }, new string[] { "<$expand>" }, null))
            {
                JsonElement result = JsonDocument.Parse(item.ToStream()).RootElement;
                Console.WriteLine(result.GetProperty("id").ToString());
                Console.WriteLine(result.GetProperty("displayName").ToString());
                Console.WriteLine(result.GetProperty("url").ToString());
            }
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools2s_AllParameters_Async()
        {
            BatchClient client = new BatchClient();

            await foreach (BinaryData item in client.GetPools2sAsync("<$filter>", new string[] { "<$select>" }, new string[] { "<$expand>" }, null))
            {
                JsonElement result = JsonDocument.Parse(item.ToStream()).RootElement;
                Console.WriteLine(result.GetProperty("id").ToString());
                Console.WriteLine(result.GetProperty("displayName").ToString());
                Console.WriteLine(result.GetProperty("url").ToString());
            }
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public void Example_GetPools2s_AllParameters_Convenience()
        {
            BatchClient client = new BatchClient();

            foreach (BatchPool item in client.GetPools2s(filter: "<$filter>", select: new string[] { "<$select>" }, expand: new string[] { "<$expand>" }))
            {
            }
        }

        [Test]
        [Ignore("Only validating compilation of examples")]
        public async Task Example_GetPools2s_AllParameters_Convenience_Async()
        {
            BatchClient client = new BatchClient();

            await foreach (BatchPool item in client.GetPools2sAsync(filter: "<$filter>", select: new string[] { "<$select>" }, expand: new string[] { "<$expand>" }))
            {
            }
        }
    }
}
