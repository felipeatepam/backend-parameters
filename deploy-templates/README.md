# backend-parameters

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

A Helm chart for Kubernetes

**Homepage:** <https://github.com/KubeRocketCI/template-python.git>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| DEV Team |  |  |

## Source Code

* <https://github.com/KubeRocketCI/template-python.git>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| autoscaling.enabled | bool | `false` |  |
| configMaps.cm-extra-config.data."application.properties" | string | `"app.mode=prod"` |  |
| configMaps.cm-extra-config.data.ENV_VAR1 | string | `"value_from_cm"` |  |
| configMaps.cm-extra-env.data.SERVER_PORT | string | `"8080"` |  |
| envFrom[0].configMapRef.name | string | `"cm-extra-env"` |  |
| envFrom[1].secretRef.name | string | `"secret-extra-env"` |  |
| env[0].name | string | `"BACKEND_PROFILES_ACTIVE"` |  |
| env[0].value | string | `"dev"` |  |
| env[1].name | string | `"ENV_VAR1"` |  |
| env[1].valueFrom.configMapKeyRef.key | string | `"ENV_VAR1"` |  |
| env[1].valueFrom.configMapKeyRef.name | string | `"cm-extra-config"` |  |
| env[2].name | string | `"ENV_VAR4"` |  |
| env[2].valueFrom.secretKeyRef.key | string | `"ENV_VAR4"` |  |
| env[2].valueFrom.secretKeyRef.name | string | `"secret-extra-config"` |  |
| env[3].name | string | `"ENV_VAR5"` |  |
| env[3].valueFrom.secretKeyRef.key | string | `"ENV_VAR5"` |  |
| env[3].valueFrom.secretKeyRef.name | string | `"backend-parameters"` |  |
| externalSecrets.backend-parameters.data[0].remoteRef.key | string | `"krci-cmtr-0oqfemca-backend-parameters"` |  |
| externalSecrets.backend-parameters.data[0].remoteRef.property | string | `"backend-parameters.ENV_VAR5"` |  |
| externalSecrets.backend-parameters.data[0].secretKey | string | `"ENV_VAR5"` |  |
| externalSecrets.backend-parameters.data[1].remoteRef.decodingStrategy | string | `"Base64"` |  |
| externalSecrets.backend-parameters.data[1].remoteRef.key | string | `"krci-cmtr-0oqfemca-backend-parameters"` |  |
| externalSecrets.backend-parameters.data[1].remoteRef.property | string | `"backend-parameters.config"` |  |
| externalSecrets.backend-parameters.data[1].secretKey | string | `"application.secret.properties.from.ps"` |  |
| fullnameOverride | string | `""` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"backend-parameters"` |  |
| image.tag | string | `""` |  |
| imagePullSecrets[0].name | string | `"regcred"` |  |
| ingress.annotations | object | `{}` |  |
| ingress.className | string | `""` |  |
| ingress.enabled | bool | `true` |  |
| ingress.hosts[0].host | string | `"edpDefault"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| ingress.tls | list | `[]` |  |
| livenessProbe.tcpSocket.port | string | `"http"` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` |  |
| podAnnotations | object | `{}` |  |
| podLabels | object | `{}` |  |
| podSecurityContext | object | `{}` |  |
| readinessProbe.initialDelaySeconds | int | `20` |  |
| readinessProbe.tcpSocket.port | string | `"http"` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| secretStore.enabled | bool | `true` |  |
| secretStore.name | string | `"aws-parameterstore"` |  |
| secretStore.region | string | `"eu-central-1"` |  |
| secrets.secret-extra-config.stringData."application.secret.properties" | string | `"secret.key=123"` |  |
| secrets.secret-extra-config.stringData.ENV_VAR4 | string | `"val4"` |  |
| secrets.secret-extra-env.stringData.ENV_VAR2 | string | `"val2"` |  |
| securityContext | object | `{}` |  |
| service.port | int | `8080` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.annotations."eks.amazonaws.com/role-arn" | string | `"arn:aws:iam::183631338639:role/krci-cmtr-0oqfemca-assume-role"` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.name | string | `"externalsecrets-aws"` |  |
| tolerations | list | `[]` |  |
| volumeMounts[0].mountPath | string | `"/config"` |  |
| volumeMounts[0].name | string | `"configmap-volume"` |  |
| volumeMounts[0].readOnly | bool | `true` |  |
| volumeMounts[1].mountPath | string | `"/secret-config"` |  |
| volumeMounts[1].name | string | `"secret-volume"` |  |
| volumeMounts[1].readOnly | bool | `true` |  |
| volumeMounts[2].mountPath | string | `"/ps-config"` |  |
| volumeMounts[2].name | string | `"ps-volume"` |  |
| volumeMounts[2].readOnly | bool | `true` |  |
| volumes[0].configMap.items[0].key | string | `"application.properties"` |  |
| volumes[0].configMap.items[0].path | string | `"application.properties"` |  |
| volumes[0].configMap.name | string | `"cm-extra-config"` |  |
| volumes[0].name | string | `"configmap-volume"` |  |
| volumes[1].name | string | `"secret-volume"` |  |
| volumes[1].secret.items[0].key | string | `"application.secret.properties"` |  |
| volumes[1].secret.items[0].path | string | `"application.secret.properties"` |  |
| volumes[1].secret.secretName | string | `"secret-extra-config"` |  |
| volumes[2].name | string | `"ps-volume"` |  |
| volumes[2].secret.items[0].key | string | `"application.secret.properties.from.ps"` |  |
| volumes[2].secret.items[0].path | string | `"application.secret.properties.from.ps"` |  |
| volumes[2].secret.secretName | string | `"backend-parameters"` |  |
