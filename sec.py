from flask import Flask, request

 
 
app = Flask(__name__)
 
 
@app.route('/secgroup', methods=['POST'])

def fun():
   
  securitygroupname = request.args.get('securitygroupname')

  protocol = request.args.get('protocol')
  priority = request.args.get('priority')
  direction = request.args.get('direction')
  sourceAddressPrefix = request.args.get('sourceAddressPrefix')
  sourcePortRange = request.args.get('sourcePortRange')
  destinationAddressPrefix = request.args.get('destinationAddressPrefix')
  destinationPortRange = request.args.get('destinationPortRange')


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
'      "networkSecurityGroupName": {\n'
'      "type": "string",\n'
'      "defaultValue": "' + str(securitygroupname) + '",\n'
'      "metadata": {\n'
'        "description": "Name of the Network Security Group"\n'
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
'    "resources": [\n'
'      {\n'
'      "type": "Microsoft.Network/networkSecurityGroups",\n'
'      "apiVersion": "2016-06-01",\n'
'      "name": "[parameters(''\'networkSecurityGroupName\''')]",\n'
'      "location": "[parameters(''\'location\''')]",\n'
'      "properties": {\n'
'        "securityRules": [\n'
'          {\n'
'            "name": "SSH",\n'
'            "properties": {\n'
'              "priority": ' + str(priority) + ',\n'
'            "protocol": "' + str(protocol) + '",\n'
'              "access": "Allow",\n'
'              "direction": "' + str(direction) + '",\n'
'              "sourceAddressPrefix": "' + str(sourceAddressPrefix) + '",\n'
'              "sourcePortRange": "' + str(sourcePortRange) + '",\n'
'              "destinationAddressPrefix": "' + str(destinationAddressPrefix) + '",\n'
'              "destinationPortRange": "' + str(destinationPortRange) + '"\n'
'            }\n'
'          }\n'
'        ]\n'
'      }\n'
'    }\n'
'  ]\n'
'}\n'
  )
 

  with open('secgroup_template.json','w') as f:
      print(data, file=f)


  return data


app.run(port=6002, host='0.0.0.0')    