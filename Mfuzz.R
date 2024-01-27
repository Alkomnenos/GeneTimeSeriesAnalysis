# 读取每个样品的表达量矩阵
Data_dir ='./data/COVID-19'
Figure_dir='./figure/COVID-19'
a=read.csv(file = file.path(Data_dir,"p4/p4_pred.csv"))

test=a[,c(3:ncol(a))]
rownames(test)=a$Gene.Name

# time-course 绘图 Mfuzz
library(ClusterGVis)

cm <- clusterData(exp = test,
                  cluster.method = "mfuzz",
                  cluster.num = 6,
                  min.std=0)

# 一键富集分析
library(org.Hs.eg.db)
# enrich for clusters
enrich <- enrichCluster(object = cm,
                        OrgDb = org.Hs.eg.db,
                        type = "BP",
                        pvalueCutoff = 0.5,
                        topn = 6,
                        seed = 5201314)

pdf(file = file.path(Figure_dir,'p4/p4_TPM_pred_c6.pdf'),height = 10,width = 10,onefile = F)
visCluster(object = cm,
           plot.type = "both",
           column_names_rot = 45,
           show_row_dend = F,
           genes.gp = c('italic',fontsize = 12,col = "black"),
           annoTerm.data = enrich,
           line.side = "left",
           go.col = rep(ggsci::pal_d3()(2),each =17),
           go.size = "pval")
dev.off()

