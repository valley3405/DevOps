# Authority
## User
UserLoginAPI = '%1{USERNAME}%2用户 登陆devEops平台'
UserCreateAPI = '%1{USER}%2 新建了新的平台用户 用户信息 %1用户名:{USERNAME}%2 名称:{FULLNAME}'
UserUpdateAPI = '%1{USER}%2 更新了平台用户信息 更新后用户信息 %1用户名:{USERNAME}%2 名称:{FULLNAME}'
UserDeleteAPI = '%1{USER}%2 删除了平台用户 删除原用户信息 %1用户名:{USERNAME}%2 名称:{FULLNAME}'
UserQRCodeAPI = '%1{USER}%2 获取了QR-CODE'

## PmnGroup
GroupCreateAPI = '%1{USER}%2 新建了权限组 新权限组信息 %1名称:{NAME}%2'
GroupUpdateAPI = '%1{USER}%2 更新了权限组 更新后信息 %1名称:{NAME}%2'
GroupDeleteAPI = '%1{USER}%2 删除了权限组 删除原信息 %1名称:{NAME}%2'

## Key
KeyCreateAPI = '%1{USER}%2 新建的密钥 密钥信息 %1名称:{NAME}%2 UUID:{UUID}'
KeyUpdateAPI = '%1{USER}%2 更新了密钥 更新后密钥信息 %1名称:{NAME}%2 UUID:{UUID}'
KeyDeleteAPI = '%1{USER}%2 删除了密钥 删除原密钥信息 %1名称:{NAME}%2 UUID:{UUID}'

## Jumper
JumperCreateAPI = '%1{USER}%2 新建了跳板机 跳板机信息 名称:{NAME} UUID:{UUID} %1连接地址:{CONNECT_IP}%2'
JumperUpdateAPI = '%1{USER}%2 更新了跳板机 更新了跳板机信息 名称:{NAME} UUID:{UUID} %1连接地址:{CONNECT_IP}%2'
JumperDeleteAPI = '%1{USER}%2 删除了跳板机 删除原跳板机信息 名称:{NAME} UUID:{UUID} %1连接地址:{CONNECT_IP}%2'

# Manager
## Group
ManagerGroupCreateAPI = '%1{USER}%2 新建了资产应用组 新建信息 %1名称:{NAME}%2 UUID:{UUID}'
ManagerGroupUpdateAPI = '%1{USER}%2 更新了资产应用组 更新后信息 %1名称:{NAME}%2 UUID:{UUID}'
ManagerGroupDeleteAPI = '%1{USER}%2 删除了资产应用组 删除原信息 %1名称:{NAME}%2 UUID:{UUID}'
ManagerGroupSelectHostAPI = '%1{USER}%2 归类部分主机进入资产应用组 %1名称:{NAME}%2 UUID:{UUID}'

## Host
ManagerHostCreateAPI = '%1{USER}%2 新建了资产主机 新建信息 %1主机:{HOSTNAME} 连接地址:{CONNECT_IP}%2 UUID:{UUID}'
ManagerHostUpdateAPI = '%1{USER}%2 更新了资产主机 更新后信息 %1主机:{HOSTNAME} 连接地址:{CONNECT_IP}%2 UUID:{UUID}'
ManagerHostDeleteAPI = '%1{USER}%2 删除了资产主机 删除原信息 %1主机:{HOSTNAME} 连接地址:{CONNECT_IP}%2 UUID:{UUID}'
ManagerHostSelectGroupAPI = '%1{USER}%2 操作了资产主机归属 %1主机:{HOSTNAME} 连接地址:{CONNECT_IP}%2 UUID:{UUID}'

# Ops
## META
OpsMetaCreateAPI = '%1{USER}%2 新建了元操作 新建信息 %1UUID:{UUID}%2'
OpsMetaUpdateAPI = '%1{USER}%2 更新了元操作 更新后信息 UUID:{UUID} %1INFO:{INFO}%2'
OpsMetaDeleteAPI = '%1{USER}%2 删除了元操作 删除原信息 UUID:{UUID} %1INFO:{INFO}%2'

## Mission
OpsMissionCreateAPI = '%1{USER}%2 新建了任务 新建信息 %1名称:{INFO}%2 UUID:{UUID}'
OpsMissionUpdateAPI = '%1{USER}%2 更新了任务 更新后信息 %1名称:{INFO}%2 UUID:{UUID}'
OpsMissionDeleteAPI = '%1{USER}%2 删除了任务 删除原信息 %1名称:{INFO}%2 UUID:{UUID}'

# Work
## Code_Work
CodeWorkCreateAPI = '%1{USER}%2 新建了工单 工单信息 %1任务名称:{MISSION} 执行缘由:{REASON}%2 UUID:{UUID}'
CodeWorkCheckAPI = '%1{USER}%2 审核了工单 工单信息 %1任务名称:{MISSION} 执行缘由:{REASON}%2 UUID:{UUID}'
CodeWorkRunAPI = '%1{USER}%2 运行了工单 工单信息 %1任务名称:{MISSION} 执行缘由:{REASON}%2 UUID:{UUID}'
CodeWorkUploadFileAPI = '%1{USER}%2 为工单上传文件 工单信息 %1任务名称:{MISSION} 执行缘由:{REASON}%2 UUID:{UUID}'

# YoCDN
YoCDNCreateAPI = '%1{USER}%2 刷新了若干CDN信息'

# EZSetup
EZSetupCreateRedisAPI = '%1{USER}%2 通过平台易装了%1Redis应用%2 安装信息 UUID:{UUID}'