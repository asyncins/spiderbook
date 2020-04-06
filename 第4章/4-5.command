# MongoDB
# 为集合 WaitCrawl 中的 url 创建 unique 约束
> db.WaitCrawl.ensureIndex({"url": 1}, {"unique": true});
{
	"createdCollectionAutomatically" : true,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}
# 插入第 1 条数据
> db.WaitCrawl.insert({"name": "exam", "url": "http://exam.com"});
WriteResult({ "nInserted" : 1 })
# 插入第 2 条数据
> db.WaitCrawl.insert({"name": "exam", "url": "http://exam.com"});
WriteResult({
	"nInserted" : 0,
	"writeError" : {
		"code" : 11000,
		"errmsg" : "E11000 duplicate key error collection: WaitCrawl.WaitCrawl index: url_1 dup key: { : \"http://exam.com\" }"
	}
})
# 插入第 3 条数据
> db.WaitCrawl.insert({"name": "exam", "url": "http://exam.com2"});
WriteResult({ "nInserted" : 1 })
# 查看集合 WaitCrawl 中的文档
> db.WaitCrawl.find();
{ "_id" : ObjectId("5dc3cd3cba05dc8f5eeac929"), "name" : "exam", "url" : "http://exam.com" }
{ "_id" : ObjectId("5dc3cdb7ba05dc8f5eeac92b"), "name" : "exam", "url" : "http://exam.com2" }