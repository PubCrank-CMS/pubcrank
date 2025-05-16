---
title: Making GraphQL Queries in Python Like a Boss
date: 2023-01-31 00:00:00 -0600
categories:
  - python
  - graphql
  - development
cover: /img/graphql.png
canonical_url: https://hackernoon.com/making-graphql-queries-in-python-like-a-boss
---

GraphQL is a newer way to create APIs that are very flexible and give users more control over how they use your API. However, with this extra control in your hands, it puts more effort on your part on how to call the GraphQL API. Unlike a REST API which you call and then receive a response determined by the API developer, with a GraphQL API, you have to develop queries to pull out information that is important to you. In Python there are several client libraries that can help you call GraphQL APIs more easily.

## GraphQL Clients

Python has a few GraphQL clients that work really well. While you can use a general HTTP call in Python or a general library like [HTTPX](https://www.python-httpx.org/) or [Requests](https://requests.readthedocs.io/en/latest/), GraphQL specific clients make it much easier to generate queries, insert variables, and listen to subscriptions. Below are few libraries I found in the past the work well.

1. [GQL](https://github.com/graphql-python/gql) is a GraphQL client that includes the most features. So if you want a way to make GraphQL queries with all the bells and whistles this library for you.
2. [Python GraphQL Client](https://github.com/prodigyeducation/python-graphql-client) is smaller client that still has support for many GraphQL features. This library has fewer dependencies and is smaller and sometimes can be easier to install if you are having version conflicts with GQL.

## Take A Different Approach: SGQLC

While Python GraphQL libraries are great and help you to generate and make queries more easily, you still have to put in the effort to figure out which queries you want to make. This means exploring your GraphQL API and deciding which parameters you want and then creating a query to pull the information out you want. [Simple GraphQL Client - SGQLC](https://github.com/profusion/sgqlc) takes a different approach. SGQLC gives you tools to generate a Python library out of a GraphQL schema. Once you have your custom library built, you can use it to make GraphQL calls even easier. Below I'll walk you through it's usage.

### 1. Download your GraphQL Schema

First download your GraphQL schema into a JSON dump.

`python3 -m sgqlc.introspection https://myapp.com/graphql schema.json`

### 2. Create a Custom Python Library

Now that you have a JSON schema you can convert it to a custom Python library.

`sgqlc-codegen schema schema.json schema.py`

### 3. Use Your Custom Library in Your Python Code

Now that you have a custom Python library, you can use Python without writing queries to call your GraphQL API.

**Selecting Default Fields**

This gets the first 100 issues from a selected repository on Github.

```python
from sgqlc.operation import Operation
from sgqlc.endpoint.requests import RequestsEndpoint

from schema import schema

# Generate a Query
op = Operation(schema.Query)
op.repository(owner=owner, name=name).issues(first=100)

# Call the endpoint
headers = {'Authorization': 'bearer TOKEN'}
endpoint = RequestsEndpoint("http://server.com/graphql", headers)

# data as a dictionary
data = endpoint(op)

# convert to Python objects
repo = (op + data).repository
for issue in repo.issues.nodes:
    print(issue)
```

The last step that converts the data to Python objects is optional. Sometimes going through large dictionaries of data can be difficult, so converting the data to Python objects can be extremely helpful.

This example selects the default fields for `issues`. This is all fields that are not relationships to other types. If you wish to change this, you can also select fields manually.

**Selecting Fields Manually**

```python
op = Operation(schema.Query)
issues = op.repository(owner=owner, name=name).issues(first=100)

# select number and title field
issues.nodes.number()
issues.nodes.title()

# selection pagination data
issues.page_info.__fields__('has_next_page')
issues.page_info.__fields__(end_cursor=True)
```

**Making a Mutation**

Calling mutations is just as easy. Below is a `login` mutation example.

```python
op = Operation(schema.Mutation)
mutation = op.login(input={'username': username, 'password': password})

# select errors and user data
mutation.errors()
mutation.user()

# call the endpoint
data = endpoint(op)
```

### Wrapping It Up

For me SGQLC takes calling GraphQL queries in Python to a whole new level of ease and compactness. I highly recommend implementing it into your Python tool belt. However, other Python libraries like GQL and Python GraphQL Client are also great tools for a more standard approach.
