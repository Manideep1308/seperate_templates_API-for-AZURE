from flask import Flask, request

 
 
app = Flask(__name__)
 
 
@app.route('/ip', methods=['POST'])

def fun():
    vmname =request.args.get('vmname')
    publicipname = request.args.get('publicipname')
    publicIPAllocationMethod =request.args.get('publicIPAllocationMethod')
    publicIPAddressVersion = request.args.get('publicIPAddressVersion')
    idleTimeoutInMinutes = request.args.get('idleTimeoutInMinutes')


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
'    "dnsLabelPrefix": {\n'
'      "type": "string",\n'
'      "defaultValue": "[toLower(format(''\'{0}-{1}\', parameters(''\'vmName\'''), uniqueString(resourceGroup().id)))]",\n'
'      "metadata": {\n'
'        "description": "Unique DNS Name for the Public IP used to access the Virtual Machine."\n'
'      }\n'
'   },\n'
'    "location": {\n'
'        "type": "string",\n'
'        "defaultValue": "[resourceGroup().location]",\n'
'        "metadata": {\n'
'          "description": "Location for all resources."\n'
'        }\n'
'      }\n'
'    },\n'  
'    "variables": {\n'
'    "publicIPAddressName": "' + str(publicipname) + '"\n'

'     },\n'
'    "resources": [\n'

'            {\n'
'      "type": "Microsoft.Network/publicIPAddresses",\n'   #pubicIp
'      "apiVersion": "2016-06-01",\n'
'      "name": "[variables(''\'publicIPAddressName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "sku": {\n'
'        "name": "Basic"\n'
'      },\n'
'      "properties": {\n'
'        "publicIPAllocationMethod": "' + str(publicIPAllocationMethod) + '",\n'
'        "publicIPAddressVersion": "' + str(publicIPAddressVersion) + '",\n'
'        "dnsSettings": {\n'
'          "domainNameLabel": "[parameters(''\'dnsLabelPrefix\''')]"\n'
'        },\n'
'        "idleTimeoutInMinutes":' +str(idleTimeoutInMinutes) + '\n'
'      }\n'
'    }\n' 
'   ]\n'
'  }\n'    

    )


    with open('publicip_template.json','w') as f:
      print(data, file=f)


    return data


app.run(port=6006, host='0.0.0.0')   