{
  template: post.html
  draft: false
  title: SQLite the New Hotness?! 🤔
  date: 2024-03-21T05:00:00.000Z
  categories:
  [
    Backend
    Database
  ]
  description: A survey of why SQLite is trending up in many places.
  cover: /img/sqlite-so-hot.jpg
  canonical_url: https://hackernoon.com/sqlite-the-new-hotness
}


SQLite is popping up in many places all the sudden as hot new tech. While it's nowhere near as hot as AI/ML right now, it is amazing that such an old technology is seeing a renaissance.

SQLite is a file based database that was initially released 23 years ago. I often tell other developers it is the fastest database but it just doesn't scale off of one server. However, because it is a file, it's extremely easy to use and also includes many advance features like full text search and GIS. Because of its ease of use, it is used in many places behind the scenes such as web browsers, operating systems, embedded applications, and more.

So why is SQLite all the rave right now? Below I'll outline some of the newest SQLite tech with a summary of why you might want to use it.

## Blockchain Powered Distributed Data

SQLite has a few distributed implementations that the Bitcoin Bros would be proud of. The [Raft protocol](https://raft.github.io/) and [Paxos protocol](https://en.wikipedia.org/wiki/Paxos_(computer_science)) are consensus protocols which can be used in blockchain like use cases. In this case, they were implemented with SQLite to create a distributed database. This helps get SQLite off of one machine and onto to many. Because of its distributed nature, the trade off is you have slower write performance. However, you gain reliability and availability. So if you want to distribute your database to multiple machines try out one of the following:

- [rqlite](https://rqlite.io/)
- [SQLite Cloud](https://sqlitecloud.io/)
- [BedrockDB](https://bedrockdb.com/)

### Usage

RQLite, SQLite, and BedrockDB are not a drop in replacement for SQLite in your application code. RQLite has an HTTP API which you can use and all have client libraries. The client libraries may be a drop in replacement for SQLite in your application code, but otherwise you will probably have to do a small lift to convert over to the appropriate client library. Additionally, Bedrock emulates MySQL. So if you can use MySQL in your application then you can also drop in BedrockDB.

## Primarily More Fun with Distributed Data

The second class of the distributed SQLite databases I've found on a high level do distributed read replicas and pass write operations to a "primary" server without use of blockchain algorithms. These implementations get you off of one machine with better write performance, in theory, than the Raft protocol implementations. Two popular implementations I found are:

- [LiteFS](https://fly.io/docs/litefs/)
- [Turso](https://turso.tech/)

### Usage

LiteFS as the name applies works more like a file system and is more a drop in replacement for your current SQLite application code. You will need to setup the replication mechanism but you will not need to change your application code. Turso requires the usage of [libSQL](https://github.com/tursodatabase/libsql) which while compatible with SQLite will require the usage of a new client library in your application code. So you will probably need some small tweaks to your application to get it working. Turso also offers an HTTP API.

## Durable SQLite

There are several solutions that allow you to replicate your SQLite database. While these solutions don't really get you off of one server unless your can configure your application for write operations to one server, they do allow you to persist your database and make it available for read replicas. You'll want to use this method if you are trying to persist your data permanently off your server or you only need one server that does the write operations and many more that do reading. This may sound similar to the previous implementations, but differs because write operations are not transparently handled. It is up to you to solve this. This could be useful in storing structured data for a pipeline or for small applications that only need one server with a way to backup your database.

There are several options for this type of solution:

- [LiteStream](https://litestream.io/)
- [Verneuil](https://github.com/backtrace-labs/verneuil)
- [LiteReplica](https://litereplica.io/)

### Usage

The good thing about this type of solution is that they are often drop in replacements for your application. You will need to setup the replication mechanism into your application but your application code will remain the same.

## Yes There's More!

Yes there are more SQLite implementations, but I found the ones I listed above more complete or easier to use right now. So keep an eye out on the SQLite space because it is moving fast.
