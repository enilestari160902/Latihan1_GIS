import shapefile

w=shapefile.Writer('soal10',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")


w.record("Moy","satu")


w.poly([[[2,1],[1,3], [6,3],[8,1]]])