#!/usr/bin/env python

def main():
   dict = {
      'Name':'Docker',
      'Status': 'Running',
      'Instance ID':'i-10000001',
      'vpc-id':'vpc-123456'
    }

   for k, v in dict.items():
      print("{0}, {1}".format(k,v))

if __name__=='__main__':
   main()
