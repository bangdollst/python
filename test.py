# -*- coding: utf-8 -*-
import base64
import md5
import urllib, urllib2, sys
import  suds


#a = 'eyJzdWNjZXNzIjpmYWxzZSwibXNnIjoi6K6i5Y2V5Y+35LiN5a2Y5Zyo77yBIiwiZXJyb3JDb2RlIjoyMDAxfQ=='
#b = base64.b64encode(a)
d = 'eyJyZXR1cm5UaW1lIjoiMjAxNy0wMy0zMSAxNDo0MTo1OCIsInJldHVybldheSI6MiAsImxvc3RSZWFzb24iOiI7VDJj5bGP5bmV5o2f5q+B5o2f5q+BMjAwO+WFheeUteWktOaNn+avgeaIluS4ouWkseaNn+avgTI15pWw5o2u57q/5o2f5q+B5oiW5Lii5aSx5o2f5q+BMjU755qu5aWX5o2f5q+B5oiW5Lii5aSx5o2f5q+BNTA7O+a7nue6s+mHkeS4ujQwXFwuMDA75a6e5LuY6LS555So5Li6MzQwXFwuMDA7IiwibG9zdEFtb3VudCI6IjM0MC4wIiwidmVuZG9yT3JkSWQiOiJDTy0xNzAzMzExNDM0MjQifQ=='
#print base64.b64encode(a)
#print b
#print base64.b64decode(d)
print base64.b64decode(d)
#print base64.b16encode(d)

#

scp = 'http://scptest.51tgt.com/tgtweb/services/businessService?wsdl'
client = suds.client.Client(scp)
print client




#host = 'http://jisushouji.market.alicloudapi.com'
#path = '/shouji/query'
#method = 'GET'
#host = 'http://ceshi.tgms.maytek.cn'#
host = 'http://tsmtest.51tgt.com'
path = '/TGMS_OssWS/heartbeat.api'
method = 'POST'
#appcode = '91558ff74e10454b8dc082a41935748a'
#querys = 'shouji=18521301228'
bodys = {}
#url = host + path + '?' + querys
url = host + path + '?'

request = urllib2.Request(url)
#request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)




def f(x):
    return x*x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
















#  public void dealOrderbillToStettle(String flightno, String shipname)
#    throws Exception
#  {
#    String SQL2 = " select * from T_TGT_SYSPARAM where number='CruisesReturnfee'";
#    List Cruieses = DbUtil.executeQuery("meta", SQL2);
#    BigDecimal brokenfee = BigDecimal.valueOf(Double.valueOf(((DataRow)Cruieses.get(0)).get("val").toString()).doubleValue());
#
#    String sql1 = "UPDATE tgt_orderbill set endTime = DATE_ADD(startTime,INTERVAL dockDays DAY) ,brokenFee = " + brokenfee + ",`status`='SETTLED',bssSynchroColumn=0 WHERE shipName = '" + shipname + "' AND flightNo = '" + flightno + "' AND `status` = 'RECEIVED'";
#    String sql2 = "UPDATE tgt_wh_equipmentpool SET equipmentStatus ='damageStatus',cruSynchroColumn ='1999-09-09' WHERE equipmentCode in(SELECT equipmentNo FROM tgt_orderbill WHERE shipName = '" + shipname + "' AND flightNo = '" + flightno + "' AND `status` = 'RECEIVED')";
#    DbUtil.executeUpdate("meta", sql1);
#    DbUtil.executeUpdate("meta", sql2);
#
#    String sql3 = "UPDATE tgt_orderbill set `status`='SETTLED',bssSynchroColumn=0 WHERE shipName = '" + shipname + "' AND flightNo = '" + flightno + "' AND `status` = 'CLOSED'";
#    DbUtil.executeUpdate("meta", sql3);
#
#    String sql4 = "UPDATE tgt_orderbill set `status`='SETTLED',bssSynchroColumn=0 WHERE shipName = '" + shipname + "' AND flightNo = '" + flightno + "' AND `status` = 'SAVE'";
#    DbUtil.executeUpdate("meta", sql4);
#
#    String sql5 = "UPDATE tgt_wh_equipmentpool SET equipmentStatus ='availableStatus',cruSynchroColumn ='1999-09-09' WHERE equipmentStatus ='inTransitStatus' AND equipmentCode in(SELECT equipmentNo FROM tgt_orderbill WHERE shipName = '" + shipname + "' AND flightNo = '" + flightno + "')";
#    DbUtil.executeUpdate("meta", sql5);
#  }
#}



























