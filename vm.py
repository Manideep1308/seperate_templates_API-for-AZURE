from flask import Flask, request

 
 
app = Flask(__name__)
 
 
@app.route('/vm', methods=['POST'])

def fun():

    vpcname = request.args.get('vpcname')
    securitygroupname = request.args.get('securitygroupname')
    subnetname = request.args.get('subnetname')
    vmname =request.args.get('vmname')
    authenticationType = request.args.get('authenticationType')
    ubuntuOSVersion = request.args.get('ubuntuOSVersion')
    vmsize = request.args.get('vmsize')
    osDiskType = request.args.get('osDiskType')
    publicipname = request.args.get('publicipname')
    nicname = request.args.get('nicname')


    



    data = (
'{\n'
'    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",\n'
'    "contentVersion": "1.0.0.0",\n'
'    "metadata": {\n'
'      "_generator": {\n'
'        "name": "bicep",\n'
'        "version": "0.5.6.12127",\n'
'        "templateHash": "12144059695652148753"\n'
'      }\n'
'    },\n'
'    "parameters": {\n' 

'    "vmName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(vmname) + '",\n'
'      "metadata": {\n'
'        "description": "The name of you Virtual Machine."\n'
'      }\n'
'    },\n'
'    "adminUsername": {\n'
'      "type": "string",\n'
'      "metadata": {\n'
'        "description": "Username for the Virtual Machine."\n'
'      }\n'
'    },\n'
'    "authenticationType": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(authenticationType) + '",\n'
'      "allowedValues": [\n'
'        "sshPublicKey",\n'
'        "password"\n'
'      ],\n'
'      "metadata": {\n'
'        "description": "Type of authentication to use on the Virtual Machine. SSH key is recommended."\n'
'      }\n'
'    },\n'
'    "adminPasswordOrKey": {\n'
'      "type": "secureString",\n'
'      "metadata": {\n'
'        "description": "SSH Key or password for the Virtual Machine. SSH key is recommended."\n'
'      }\n'
'    },\n'

'    "ubuntuOSVersion": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(ubuntuOSVersion) + '",\n'
'      "allowedValues": [\n'
'        "12.04.5-LTS",\n'
'        "14.04.5-LTS",\n'
'        "16.04.0-LTS",\n'
'        "18.04-LTS",\n'
'        "20.04-LTS"\n'
'      ],\n'
'      "metadata": {\n'
'        "description": "The Ubuntu version for the VM. This will pick a fully patched image of this given Ubuntu version."\n'
'      }\n'
'    },\n'  
'    "vmSize": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(vmsize) + '",\n'
'      "metadata": {\n'
'        "description": "The size of the VM"\n'
'      }\n'
'    },\n'
'    "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'
'    "variables": {\n'

'     "networkInterfaceName": "' + str(nicname) + '",\n'
'    "osDiskType": "' + str(osDiskType) + '",\n'
'    "linuxConfiguration": {\n'
'      "disablePasswordAuthentication": true,\n'
'      "ssh": {\n'
'        "publicKeys": [\n'
'          {\n'
'            "path": "[format(''\'/home/{0}/.ssh/authorized_keys\', parameters(''\'adminUsername\'''))]",\n'
'            "keyData": "[parameters(''\'adminPasswordOrKey\''')]"\n'
'          }\n'
'        ]\n'
'      }\n'
'    }\n'
'  },\n'
'    "resources": [\n'

'        {\n'
'      "type": "Microsoft.Compute/virtualMachines",\n'      #virtualmachine
'      "apiVersion": "2021-11-01",\n'
'      "name": "[parameters(''\'vmName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "hardwareProfile": {\n'
'          "vmSize": "[parameters(''\'vmSize\''')]"\n'
'        },\n'
'        "storageProfile": {\n'
'          "osDisk": {\n'
'            "createOption": "FromImage",\n'
'            "managedDisk": {\n'
'              "storageAccountType": "[variables(''\'osDiskType\''')]"\n'
'            }\n'
'          },\n'
'          "imageReference": {\n'
'            "publisher": "Canonical",\n'
'            "offer": "UbuntuServer",\n'
'            "sku": "[parameters(''\'ubuntuOSVersion\''')]",\n'
'            "version": "latest"\n'
'          }\n'
'        },\n'
'         "networkProfile": {\n'
'          "networkInterfaces": [\n'
'            {\n'
'              "id": "[resourceId(''\'Microsoft.Network/networkInterfaces\', variables(''\'networkInterfaceName\'''))]"\n'
'            }\n'
'          ]\n'
'        },\n'
'        "osProfile": {\n'
'          "computerName": "[parameters(''\'vmName\''')]",\n'
'          "adminUsername": "[parameters(''\'adminUsername\''')]",\n'
'          "adminPassword": "[parameters(''\'adminPasswordOrKey\''')]",\n'
'          "linuxConfiguration": "[if(equals(parameters(''\'authenticationType\'''), ''\'password\'''), null(), variables(''\'linuxConfiguration\'''))]"\n'
'        }\n'
'       }\n'        
'      }\n'
'  ]\n'
'}\n'
 )

    with open('vmnetworkinterface_template.json','w') as f:
        print(data, file=f)
 

    return data

app.run(port=6004, host='0.0.0.0')      