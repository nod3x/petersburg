#!/usr/bin/env python
#
#@author: Chuka Okoye
#Copyright info here
#
#


import lazyboy
from thrift import Thrift
from cassandra import Cassandra
from cassandra.ttypes import *
import time

client = lazyboy.connection.Client(['localhost:9160'])

def main():
   keyspace = "Twitter"
   column_path = ColumnPath(column_family="Timeline",column="message")
   key = "pinggoat"
   value = "hello world!, my first cassandra input"
   timestamp = time.time()
   consistency = ConsistencyLevel.ONE
   column_parent = ColumnParent(column_family="Timeline")
   column_names = list("message")
   slice_predicate =\
   SlicePredicate(column_names,SliceRange(start='',finish='',reversed=False,count=100))
   
   #Insert data into cassandra database with already defined schema

   try:
      client.insert(keyspace,key,column_path,value,timestamp,consistency)
   except Thrift.TException, tex:
      print 'Thrift: %s' % tex.message

   #Now retrieve data from cassandra database
   try:
      data = client.get_slice(keyspace,key,column_parent,\
                              slice_predicate,consistency)
      print "hello"
   except Thrift.TException, tex:
      print 'Thrift %s' % tex.message

if __name__ == '__main__':
   print "Running cassandra program\n"
   main()