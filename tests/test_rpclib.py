# coding=utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

"""
import time

from kazoo.client import KazooClient

from dubbo_client import ZookeeperRegistry, DubboClient, DubboClientError, ApplicationConfig

__author__ = 'caozupeng'


def my_zk():
    config = ApplicationConfig('test_rpclib')
    service_interface = 'com.yytcloud.platform.service.api.IApplicationQueryService'
    # 该对象较重，有zookeeper的连接，需要保存使用
    registry = ZookeeperRegistry('10.188.181.146:2181', config)
    # registry = MulticastRegistry('224.5.6.7:1234', config)
    user_provider = DubboClient(service_interface, registry, version='1.0.0',group='usertest_yytcloud_default')
    for i in range(1000):
        try:
            pk=user_provider.call("queryAllApplication")
            # pk = user_provider.queryCorpList()
            print(pk)
            # print(user_provider.getUserByCode('wuzq'))
            # print user_provider.getUser(123)
            # print user_provider.queryUser(
            #     {u'age': 18, u'time': 1428463514153, u'sex': u'MAN', u'id': u'A003', u'name': u'zhangsan'})
            # datas = user_provider.queryAll()
            # for key, user in datas.items():
            #     print user['name']
            # print user_provider.isLimit('MAN', 'Joe')
            # print user_provider('getUser', 'A005')
            # print user_provider.notFunc()
            # print user_provider.gotException()
        except DubboClientError as client_error:
            print(client_error.message)
            print(client_error.data)
        time.sleep(5)
def ka_client():
    zk = KazooClient(hosts='10.188.181.146:2181')
    zk.start()
    parent_node = '{0}/{1}/{2}'.format('dubbo', 'com.yytcloud.platform.service.api.IApplicationQueryService', '')
    nodes = zk.get_children(parent_node)
    print(len(nodes))
if __name__ == '__main__':
    my_zk()