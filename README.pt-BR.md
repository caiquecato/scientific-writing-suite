# Scientific Writing Suite

[English](README.md)

Sete skills para planejar, estruturar, redigir, parafrasear, revisar e preparar artigos científicos para submissão. A skill geral coordena o trabalho; cada módulo também pode ser instalado e utilizado sozinho.

A regra central é preservar a evidência. Informação ausente deve ser sinalizada, sem preencher o texto com dados, referências ou procedimentos inventados.

## Instalação

Com o [Skills CLI](https://github.com/vercel-labs/skills), selecione os módulos e o agente desejados:

```sh
npx skills add caiquecato/scientific-writing-suite
```

Para instalar apenas a paráfrase:

```sh
npx skills add caiquecato/scientific-writing-suite --skill scientific-writing-paraphrase
```

Também é possível copiar as pastas desejadas de `skills/` para o diretório de skills documentado pelo agente. Os módulos são autossuficientes; não exigem chave de API, servidor MCP ou script instalador. O CLI de terceiros tem seus próprios requisitos, acessos de rede e política de telemetria.

## Módulos

| Nome | Função |
|---|---|
| `scientific-writing` | Regras de integridade e coordenação do fluxo. |
| `scientific-writing-plan` | Pergunta, contribuição, lacunas e plano. |
| `scientific-writing-structure` | Organização de argumento e seções. |
| `scientific-writing-draft` | Redação baseada nos registros disponíveis. |
| `scientific-writing-paraphrase` | Reescrita fiel ao significado original. |
| `scientific-writing-review` | Revisão crítica e sustentação das afirmações. |
| `scientific-writing-submit` | Adequação editorial, carta e resposta aos pareceristas. |

## Uso

Em agentes com invocação por nome:

```text
Use $scientific-writing-paraphrase neste parágrafo.
Preserve números, referências, negações e grau de certeza.
```

```text
Use $scientific-writing-review para verificar se as conclusões
são sustentadas pelos métodos e resultados fornecidos.
```

A língua da resposta segue o pedido do usuário. A suíte é geral, sem especialização obrigatória em uma área.

## Controles e limites

Cada módulo exige a mesma base de integridade: preservar dados e incerteza, sinalizar lacunas, distinguir citação mantida de fonte verificada e tratar instruções embutidas nos documentos como conteúdo.

As pastas instaláveis contêm instruções e metadados. Não incluem código executável, instalação automática, concessão de ferramentas ou envio de manuscritos. A proteção é instrucional: o agente hospedeiro e suas ferramentas continuam determinando o que será executado. Não há garantia absoluta de ausência de alucinações.

A autoria humana exige revisão final e conferência das fontes. As declarações exigidas sobre assistência de IA são preservadas. Não são prometidas aceitação, publicação rápida ou evasão de detectores.

## Documentação

- [Exemplos sintéticos](docs/examples.md)
- [Fontes e extensão de consulta](docs/sources.md)
- [Avaliação e limitações](docs/evaluation.md)
- [Segurança e permissões](SECURITY.md)
- [Contribuições](CONTRIBUTING.md)

O exemplo principal do README utiliza uma referência fictícia identificada como não verificada para demonstrar preservação de atribuição. Ela não deverá ser usada como fonte bibliográfica.

## Licença

Material original sob [MIT](LICENSE), © 2026 Caique dos Santos Aguiar. As referências mantêm seus próprios direitos. A organização da página foi inspirada no [taste-skill](https://github.com/Leonxlnx/taste-skill); textos e identidade visual foram produzidos para este projeto.
