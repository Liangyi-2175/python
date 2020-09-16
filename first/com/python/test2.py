# # for x in range(10,0,-2):
# # #     print(x,end='|')
# # # a=[1,2,3,4,5,6,7,8]
# # # for x in range(0,len(a),2):
# # #     print(a[x])
# #
# # a=[1,2,3,4,5,6,7,8]
# # b=a[0:len(a):2]
# # print
# import requests
# import pyapollo
# config_server_url = 'http://47.110.5.120:18022'
# appId = "jyxb-main"
# env = "DEV"
# cluster = "default"
# namespaceName = "application"
# url = '{}/configfiles/json/{}/{}/{}?ip={}'.format(config_server_url, appId, cluster, namespaceName)
# #url = config_server_url+"/configfiles/json/"+appId+"/"+clusterName+"/"+namespaceName
# print(url)
# response = requests.get(url)
# print(response)

a = {}
a['test']={}
print(a)
a['test']={'q':2,'w':3}

print(a)

