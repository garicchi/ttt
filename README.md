# ttt
ttt: togai tsv tool

## INSTALL

required python 3.6 or later
```
pip install git+https://github.com/garicchi/ttt.git
```

## VIEW

sample.tsv
```
col1	col2	col3
val1-1	val2-1	val3-1
val2-1	val2-2	val2-3
val3-1	val3-2	val3-3
```

tsvテーブルを表示
```
$ ttt view sample/sample.tsv 
col1  	col2  	col3  
val1-1	val2-1	val3-1
val2-1	val2-2	val2-3
val3-1	val3-2	val3-3
```

ヘッダーを表示

```
$ ttt view --header sample/sample.tsv 
col1  
col2  
col3  
```

カラムを絞り込み
```
$ ttt view -c col2 -c col3 sample/sample.tsv 
col2  	col3  
val2-1	val3-1
val2-2	val2-3
val3-2	val3-3
```

昇順ソート
```
$ ttt view -s col2 sample/sample.tsv 
col1  	col2  	col3  
val1-1	val2-1	val3-1
val2-1	val2-2	val2-3
val3-1	val3-2	val3-3
```

降順ソート
```
$ ttt view -s col2 -r sample/sample.tsv 
col1  	col2  	col3  
val3-1	val3-2	val3-3
val2-1	val2-2	val2-3
val1-1	val2-1	val3-1
```

テーブルのjoin
sample02.tsv
```
other1	other2
val1-1	other-2-1
val2-1	other-2-2
val3-1	other-2-3
```
```
$ ttt view -on col1=other1 sample/sample.tsv sample/sample02.tsv 
col1  	col2  	col3  	other1	other2   
val1-1	val2-1	val3-1	val1-1	other-2-1
val2-1	val2-2	val2-3	val2-1	other-2-2
val3-1	val3-2	val3-3	val3-1	other-2-3
```
