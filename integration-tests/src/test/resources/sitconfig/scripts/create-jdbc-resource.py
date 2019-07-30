# Copyright 2019, Oracle Corporation and/or its affiliates.  All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.
  
def createDataSource(dsName):
    edit()
    startEdit()
    cd('/')
    cmo.createJDBCSystemResource(dsName)
    cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName)
    cmo.setName(dsname)
    
    cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDataSourceParams/'+dsName)
    set('JNDINames',jarray.array([String('jdbc/'+dsName)], String))
    
    cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName)
    cmo.setDatasourceType('GENERIC')
    
    cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDriverParams/'+dsName)
    cmo.setUrl('jdbc:mysql://HOST:31306')
    
    cmo.setDriverName('com.mysql.jdbc.Driver')
    set('PasswordEncrypted', dsPassword)
    
    cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCConnectionPoolParams/'+dsName)
    cmo.setTestTableName('SQL SELECT 1\r\n\r\n')
    
    cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDriverParams/'+dsName+'/Properties/'+dsName)
    cmo.createProperty('user')
    
    cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDriverParams/'+dsName+'/Properties/'+dsName+'/Properties/user')
    cmo.setValue('root')
    
    cd('/JDBCSystemResources/'+dsName+'/JDBCResource/'+dsName+'/JDBCDataSourceParams/'+dsName)
    cmo.setGlobalTransactionsProtocol('OnePhaseCommit')
    
    cd('/JDBCSystemResources/'+dsName)
    set('Targets',jarray.array([ObjectName('com.bea:Name=cluster-1,Type=Cluster')], ObjectName))
    
    save()    
    activate()    

connect('weblogic', 'welcome1', 't3://HOST:7001')
createDataSource('JdbcTestDataSource-1')
disconnect()
exit()