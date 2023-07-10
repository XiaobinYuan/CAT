# Dice Helm Chart

The helm chart is a  demo to showcase to CAT.

## Deployment

### Prerequisites

Prerequisites to installing this helm chart and having it function are to have:

1. A ck8s luster
1. `kubectl` configured with the correct `~/.kube/config` to work with said cluster
1. Helm 3 available in your path as `helm`

### Deployment Commands

1. `git clone git@github.com:XiaobinYuan/CAT.git`
1. `cd Chart/dice`
1. `kubectl create namespace dice`
1. `helm -n dice install --atomic dice .`
