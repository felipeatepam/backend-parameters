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
| affinity | object | `{}` | https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity |
| autoscaling.enabled | bool | `false` |  |
| autoscaling.maxReplicas | int | `100` |  |
| autoscaling.minReplicas | int | `1` |  |
| autoscaling.targetCPUUtilizationPercentage | int | `80` |  |
| configMaps.cm-extra-config.data."application.properties" | string | `"server.port=8080\nlogging.level.root=INFO\n"` |  |
| configMaps.cm-extra-config.data.ENV_VAR1 | string | `"value1"` |  |
| configMaps.cm-extra-env.data.LOGGING_LEVEL_ROOT | string | `"INFO"` |  |
| configMaps.cm-extra-env.data.SERVER_PORT | string | `"8080"` |  |
| envFrom[0].configMapRef.name | string | `"cm-extra-env"` |  |
| envFrom[1].secretRef.name | string | `"secret-extra-env"` |  |
| env[0].name | string | `"ENV_VAR5"` |  |
| env[0].valueFrom.secretKeyRef.key | string | `"ENV_VAR5"` |  |
| env[0].valueFrom.secretKeyRef.name | string | `"backend-parameters"` |  |
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
| image.tag | string | `""` | Overrides the image tag whose default is the chart appVersion. |
| imagePullSecrets[0].name | string | `"regcred"` |  |
| ingress.annotations | object | `{}` |  |
| ingress.className | string | `""` |  |
| ingress.dnsWildcard | string | `"development.krci-dev.cloudmentor.academy"` |  |
| ingress.enabled | bool | `true` |  |
| ingress.hosts[0].host | string | `"edpDefault"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| ingress.tls | list | `[]` |  |
| livenessProbe.tcpSocket.port | string | `"http"` |  |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` | https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector |
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
| secrets.secret-extra-config.stringData."application.secret.properties" | string | `"secret.key=123456\n"` |  |
| secrets.secret-extra-config.stringData.ENV_VAR4 | string | `"value4"` |  |
| secrets.secret-extra-env.stringData.ENV_VAR2 | string | `"value2"` |  |
| secrets.secret-extra-env.stringData.ENV_VAR3 | string | `"value3"` |  |
| securityContext | object | `{}` |  |
| service.port | int | `8080` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.annotations | object | `{}` | Annotations to add to the service account |
| serviceAccount.annotations."eks.amazonaws.com/role-arn" | string | `"arn:aws:iam::183631338639:role/krci-cmtr-0oqfemca-assume-role"` |  |
| serviceAccount.automount | bool | `true` | Automatically mount a ServiceAccount's API credentials? |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.create | bool | `true` | Specifies whether a service account should be created |
| serviceAccount.name | string | `""` | The name of the service account to use. If not set and create is true, a name is generated using the fullname template |
| serviceAccount.name | string | `"externalsecrets-aws"` |  |
| tolerations | list | `[]` | https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ |
| volumeMounts[0].mountPath | string | `"/ps-config"` |  |
| volumeMounts[0].name | string | `"ps-volume"` |  |
| volumeMounts[0].readOnly | bool | `true` |  |
| volumes[0].name | string | `"ps-volume"` |  |
| volumes[0].secret.items[0].key | string | `"application.secret.properties.from.ps"` |  |
| volumes[0].secret.items[0].path | string | `"application.secret.properties.from.ps"` |  |
| volumes[0].secret.secretName | string | `"backend-parameters"` |  |
