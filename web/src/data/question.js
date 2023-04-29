const question_list = [
	"怎么治蛋白丢失性胃肠病？",
	"如何可以不患上透明细胞汗腺腺瘤？",
	"医治先天性后鼻孔闭锁的方法是什么？",
	"怎样才能免得肠石性肠梗阻？",
	"怎么才不会得沙门氏菌属食物中毒？",
	"如何可以不患上药物性肝病？",
	"咋才可不患上胰高血糖素瘤？",
	"咋才可以不患上鼻前庭炎？",
	"阴道美丽筒线虫病的成因是什么？",
	"怎么才不会患上妊娠期肝内胆汁淤积症？",
	"咋样才能不得热咳？",
	"过敏性皮炎的成因是什么？",
	"眼睑痉挛-口下颏部肌张力障碍会导致什么？",
	"怎么才不会患上远视呢？",
	"脓胸是由于什么原因引起的呢？",
	"怎么才可以不患上食管受压性吞咽困难呢？",
	"淋巴管炎是什么引起的呢？",
	"咋样才可以不患上原藻病？",
	"怎么才可以不患上女性尿道癌呢？",
	"眼丹是什么原因导致的？",
	"怎样才不会患上单侧关节突关节脱位？",
	"子嗽和哪些症状一同发生？",
	"有哪些方法可以不患混合性厌氧菌感染？",
	"患有外阴神经鞘瘤应该采用哪种治疗方法？",
	"如何可以避免患上急性中耳炎？",
	"怎样才能避免患上右心室双出口？",
	"怎样才能不患呼吸机相关性肺炎？",
	"妊娠期肝内胆汁淤积症应该采用哪些治疗方式？",
	"常见丝虫病有哪些症状？",
	"绒毛膜上皮癌伴随哪些症状发生？",
	"如何处理婴儿腹部远心性脂肪营养不良？",
	"医源性胆管损伤会导致哪些症状？",
	"胃肠型食物中毒应该采取哪些治疗措施？",
	"怎么治冠状动脉终止异常？",
	"高颅压性脑积水有哪些表征？",
	"怎么样才能避免颈椎椎弓裂？",
	"干酵母片有什么用途？",
	"颠茄磺苄啶片用于治疗哪些疾病？",
	"甘露消毒丸主要用于治疗什么疾病？",
	"复方磺胺甲噁唑片可以治疗哪些疾病？",
	"穿心莲片通常用来做什么？",
	"维生素B1丸的批准文号是什么？",
	"大黄碳酸氢钠片通常用于什么情况下？",
	"非诺贝特片能够治愈哪些疾病？",
	"藿香正气水主要用于治疗什么疾病？",
	"固本益肠胶囊有什么功效？",
	"杞菊地黄丸的主治疾病是什么？",
	"苯妥英钠片可以治疗哪些疾病？",
	"维U颠茄铝胶囊主要用于治疗哪些疾病？",
	"阿莫西林胶囊有什么用途？",
	"盐酸赛庚啶片通常用于什么情况下？",
	"替莫唑胺胶囊的批准证文号是什么？",
	"知柏地黄丸通常用于什么情况下？",
	"烟酸片的主要用途是什么？",
	"盐酸苯海拉明片通常用来治疗哪些疾病？",
	"清胰利胆颗粒的主要作用是什么？",
	"水杨酸甲酯气雾剂有什么好处？",
	"冰硼咽喉散有何作用？",
	"维生素B1片有什么用途？",
	"头孢克肟片的用途是什么？",
	"牛黄解毒片的准字号是什么？",
	"麝香接骨胶囊通常用来治疗哪些疾病？",
	"醋酸泼尼松片需要医生处方才能购买吗？",
	"牛黄解毒丸主要用于治疗哪些疾病？",
	"喷托维林氯化铵糖浆的主要治疗对象是什么？",
	"利福平胶囊有何益处？",
	"伤湿祛痛膏治疗什么疾病？",
	"脑心舒口服液有什么用处？",
	"咳喘宁的批号是什么？",
	"氨茶碱片的准字号是多少？",
	"补肾强身片的批准证号是什么？",
	"乙酰螺旋霉素片的批准证号是什么？",
	"氨咖黄敏片主治什么疾病？",
	"石淋通颗粒用于治疗什么疾病？",
	"强力定眩胶囊有什么用处？",
	"复方磺胺甲噁唑片主治什么疾病？",
	"需要利培酮口服液吗？",
	"五味子糖浆主治什么疾病？",
	"甲硝唑片用于治疗什么疾病？",
	"牡蛎碳酸钙片的准字号是什么？",
	"调中四消丸用来做什么？",
	"复方丹参片有什么好处？",
	"复方杏香兔耳风片有批文吗？",
	"乙酰螺旋霉素片有什么用处？",
	"盐酸奈福泮片医治什么疾病？",
	"复方利血平片有什么用处？",
	"养血安神糖浆用来做什么？",
	"醋酸曲安西龙尿素乳膏主治什么疾病？",
	"安乃近片的批准号是什么？",
	"复方满山白颗粒有什么用处？",
	"消咳喘分散片有什么用处？",
	"酚氨咖敏胶囊的批准号是什么？",
	"米格来宁片有何用处？",
	"玉泉胶囊主治什么疾病？",
	"头孢氨苄胶囊有批文吗？",
	"利用什么方法可以避免放射病的症状？",
	"肝脏局灶性结节性增生的病症状有哪些？",
	"如何避免肺脓肿？",
	"胆囊良性肿瘤会出现哪些病表现？",
	"焦油性黑变病应该如何避免？",
	"什么因素会导致粪类圆线虫病？",
	"怎样可以不出现窦性期前收缩？",
	"怎么才能避免卵泡腺细胞增殖综合征？",
	"老年人低血糖症会因为什么而出现？",
	"葡萄膜病的治疗方式有哪些？",
	"先天性胆管囊状扩张的原因是什么？",
	"什么因素会导致嗜酸性粒细胞白血病？",
	"急进性肾小球肾炎是由什么引起的？",
	"阴茎纤维性海绵体炎是怎么引起的？",
	"蚂蚁叮咬和什么症状一同出现？",
	"如何治疗甲状腺功能减低所致贫血？",
	"鳞状毛囊角化病的治疗方式有哪些？",
	"单侧肺气肿的原因是什么？",
	"绝经期尿路感染会引起哪些现象？",
	"肺组织细胞增生症和哪些病症一同发生？",
	"怎样避免喉淀粉样变？",
	"难治性癫痫可以用什么方法治疗？",
	"怎么抵御阿片中毒？",
	"疱疹样脓疱病会出现哪些病症候？",
	"食管受压性吞咽困难应该如何抵御？",
	"卡普兰综合征的治疗方法有哪些？",
	"痈疮的主治方法有哪些？",
	"如何避免口腔念珠菌病？",
	"脑外伤后综合征会有哪些病症候？",
	"怎样才能避免肝上皮样血管内皮细胞瘤的出现？",
]

const get_question = () => {
	return question_list[Math.floor(Math.random() * question_list.length)]
}

export default get_question
