# GitOps Options Quick Notes

## Argo CD
- UI focused, strong app-of-apps patterns
- Good for complex multi-app deployments
- Common with Helm or Kustomize

## Flux
- GitOps-first CLI and Git-based workflows
- Strong with multi-tenant clusters
- Works well with Kustomize and Helm Controller

## Deployment Strategies
- Rolling update: default for many services
- Blue/green: instant cutover, needs extra capacity
- Canary: gradual traffic shift with metrics gates

## Promotion Gates
- Require image scan pass
- Require policy check pass
- Require smoke test pass
