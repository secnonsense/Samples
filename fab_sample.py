from fabric import SerialGroup
result = SerialGroup('1.1.1.1','2.2.2.2').run('hostname')
