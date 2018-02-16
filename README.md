# Product-matching

Running instruction<br/>
1）Put prod_match.py, products.txt and listings.txt into the same folder.<br/>
2) Use Python prod_match.py to run program. <br/>
3) A "results.txt" will be generated in the same folder.<br/>

Description<br/>
This program can match a list of product to a sepcific product name.<br/>

Input Files<br/>
1) products.txt: Text file with one Product object per line.<br/>
Example of Product Object:<br/>
{
"product_name": String,
"manufacturer": String,
"family": String,
"model": String,
"announced-date": String
}

2) listings.txt:Text file with one List object per line.<br/>
Example of List Object:<br/>
{
"title": String,
"manufacturer": String,
"currency": String,
"price": String
}

Output File<br/>
1) results.txt: text file with one Result object per line.<br/>
Example of Result Object:<br/>
{
"product_name": String,
"listings": Array[Listing]
}
