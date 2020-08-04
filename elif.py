# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:21:47 2020

@author: POINT
"""


aclNum=int(input("what i the IPv4 ACL number"))
aclNum=int(acl)
if aclNum>=1 and aclNum <=99:
    print ("this is a standar IPv4 ACL.")
elif aclNum >=100 and aclNum <=199:
    print ("this is a extended IPv4 ACL.")
else:
    print ("this is not number ACL")    
