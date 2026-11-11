# Revisão jurídica do Scientific Writing Suite

Data: 11 de novembro de 2026.
Revisão pública examinada: `11687d66890798b2ea0c8e8adf5fac67b1e23717` (0.1.1).
Ajustes desta revisão: distribuição 0.1.2.

## Conclusão e alcance

Não foi identificado achado crítico ou alto confirmado no material examinado. Foi identificada uma lacuna documental de gravidade média na distribuição isolada dos módulos: o texto completo da licença MIT ficava apenas na raiz do repositório. A lacuna foi corrigida com uma cópia da licença em cada módulo e testes de regressão.

Não se recomenda apagar as referências científicas. O uso de fontes para formular instruções próprias foi distinguido da reprodução de textos protegidos. Não foi encontrada distribuição dos PDFs, figuras ou tabelas dos artigos nos arquivos versionados. Essa constatação não equivale a uma comparação pericial de todas as frases com todas as fontes.

Esta é uma revisão técnica documental, sem valor de parecer jurídico ou certificação de conformidade. Permanecem limitações sobre direitos de terceiros, contribuição humana em material assistido por IA, operação das plataformas e uso em outras jurisdições.

## Perfil e método

Foi examinada a árvore de arquivos versionados da revisão indicada, confirmada também na branch pública. Foram incluídos os sete módulos, documentação, exemplos, respostas sintéticas, licença, imagem SVG, metadados e rotina de validação. Os diretórios locais de pesquisa, arquivos temporários e instalações pessoais não integram este objeto.

A triagem da *skill* `blindagem-juridica` foi executada sobre uma cópia somente dos arquivos versionados. Os alertas foram confrontados com o código. Foram consultadas fontes oficiais de legislação, licenças e termos das plataformas; quatro páginas de artigos PLOS foram reconferidas como amostra das licenças declaradas.

O projeto distribui instruções gratuitamente e não implementa cadastro, cobrança, armazenamento de manuscritos ou serviço de análise hospedado pelo mantenedor. Os testes apresentados usam dados declarados sintéticos. As referências bibliográficas e a identidade pública do mantenedor não devem ser confundidas com uma base de participantes reais.

## Fundamentos considerados

A Lei 9.610/1998 distingue ideias e métodos da expressão protegida, reconhece direitos de autoria e estabelece condições para reprodução e citação. A existência de uma referência não concede autorização irrestrita para copiar uma obra. Foram consultados os arts. 7º, § 3º, 8º, 11, 24, 29 e 46. [Texto atualizado da Câmara dos Deputados](https://www2.camara.leg.br/legin/fed/lei/1998/lei-9610-19-fevereiro-1998-365399-normaatualizada-pl.html).

A MIT exige a preservação dos avisos de direitos autorais e permissão nas cópias ou partes substanciais abrangidas. O pedido de citação acadêmica não foi tratado como restrição adicional à licença. [Texto da MIT na OSI](https://opensource.org/license/mit).

As condições Creative Commons dependem da licença e versão efetivamente aplicáveis. A referência a uma obra, isoladamente, não transfere seus direitos ao repositório. [Texto legal CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.pt). Não foi presumida uma licença única para todas as fontes.

A aplicabilidade da LGPD depende do tratamento realizado. A ausência de um serviço próprio de coleta não dispensa a avaliação de tratamentos que o mantenedor venha efetivamente a realizar. Foram considerados os arts. 3º, 5º, 6º, 7º e 46. [LGPD atualizada](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html).

## Achado corrigido

### J01 — Licença ausente das pastas instaláveis

Gravidade: média, como lacuna de distribuição e rastreabilidade de permissões; não foi concluída uma infração consumada.

Antes da correção, as pastas instaláveis continham apenas `SKILL.md` e `agents/openai.yaml`. A declaração `license: MIT` identificava a licença, mas a instalação seletiva podia omitir o aviso completo presente na raiz.

Foram incluídos sete arquivos `skills/*/LICENSE`, idênticos ao texto da raiz. O validador passou a exigir sua presença e correspondência. Dois testes reproduzem a ausência ou divergência desses avisos. O texto da MIT e as instruções científicas não foram modificados.

## Esclarecimentos documentais aplicados

Em `THIRD_PARTY_NOTICES.md`, foi esclarecido que a MIT abrange somente direitos que os contribuidores possam licenciar; referências e marcas de terceiros não são relicenciadas. Foi distinguido o pedido acadêmico de citação de uma condição adicional de uso. Também foi explicitado que citar autores ou plataformas não representa endosso ou certificação.

Os dois READMEs foram ajustados para informar que os módulos incluem o texto da licença. A política de não redistribuir artigos, a bibliografia e os avisos de limitações foram preservados. Não foram criadas políticas fictícias de privacidade, cookies ou reembolso para funcionalidades inexistentes.

## Tabela 1. Verificação dos 17 itens

| Item | Estado no escopo | Evidência ou limite |
|---|---|---|
| 1. Política de privacidade própria | Não aplicável ao fluxo implementado | Não há serviço próprio de coleta. GitHub e agente hospedeiro têm operações próprias; não foi declarada isenção geral de LGPD. |
| 2. Condições de uso e licença | Verificado no escopo | MIT na raiz e nos módulos; permissões e limites de terceiros esclarecidos. |
| 3. Gestão de cookies própria | Não aplicável ao artefato | Não há aplicação web própria nem mecanismo de cookies implementado no repositório. |
| 4. Reembolso e arrependimento | Não aplicável ao fluxo implementado | Não foi identificado pagamento ou contrato de venda. |
| 5. Formulários de dados | Não aplicável ao artefato | Não há formulário ou *endpoint* de coleta implementado. |
| 6. Minimização | Verificado no escopo | Exemplos sintéticos; ausência de bases reais de participantes nos arquivos versionados examinados. |
| 7. Rastreamento próprio | Verificado no escopo | Sem código de rastreamento nos módulos. *Badges* externos e CLI de terceiros estão identificados. |
| 8. Acessibilidade geral | Parcial | Estrutura em *Markdown* e imagem com descrição; não foram testadas tecnologias assistivas ou a interface completa do GitHub. |
| 9. Texto alternativo | Verificado no escopo | As imagens do README têm atributos alt; o SVG contém título e descrição. |
| 10. Contraste da imagem própria | Verificado no escopo limitado | Cálculo das cores de texto do *banner* registrado nesta revisão; não abrange os componentes do GitHub. |
| 11. Teclado em interface própria | Não aplicável ao artefato | Não há controles interativos próprios. A navegação da plataforma não foi certificada. |
| 12. Depoimentos e avaliações | Verificado no escopo | Não há depoimentos de clientes; resultados de testes são apresentados como exploratórios. |
| 13. Promessas de resultado | Verificado no escopo | Não são prometidas aceitação, ausência de alucinações ou evasão de detectores; limitações constam do README e da avaliação. |
| 14. Direitos autorais e licenças | Parcial, com J01 corrigido | Licenças dos módulos completas e atribuições mantidas; não houve perícia de similaridade com todas as fontes. |
| 15. Identificação comercial | Não aplicável ao fluxo implementado | Projeto gratuito sem *checkout*; autoria e perfil do mantenedor estão identificados. Não foi presumida exigência de CNPJ. |
| 16. Governança de dados | Parcial | Orientações contra divulgação de manuscritos privados e dados pessoais; práticas fora do código não foram auditadas. |
| 17. Outros riscos | Parcial | Limites de direitos sobre material assistido por IA e ausência de endosso esclarecidos; marcas e jurisdições estrangeiras não foram exauridas. |

A Tabela 1 contém sete itens verificados dentro do escopo, seis não aplicáveis ao fluxo implementado e quatro parcialmente avaliados. Esses estados não representam certificação jurídica.

## Artigos, atribuição e direitos de terceiros

As páginas de [Mensh e Kording](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619), [Zhang](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003453), [Noble](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005730) e [Pautasso](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003149) exibem licença de atribuição Creative Commons. Foram mantidas referências aos autores e às obras; não foi autorizada, por esta revisão, a reprodução integral desses trabalhos.

O PDF de Hites não está no repositório público. As demais fontes, inclusive cópias acadêmicas, políticas editoriais e versões no arXiv, permanecem como referências sob seus próprios direitos. Disponibilidade pública e acesso aberto não foram tratados como autorização universal de reprodução.

O *banner* foi produzido para o projeto; não contém fotografias ou arquivos de fontes incorporados. A indicação de Arial e Georgia no SVG referencia fontes do sistema. Não foi identificada cópia de imagem ou código do taste-skill; sua organização serviu como referência de apresentação. Não se realizou busca de anterioridade de marcas no INPI.

## IA, autoria e divulgação

Os termos consultados da OpenAI atribuem ao usuário os direitos que a empresa eventualmente detenha sobre saídas, dentro dos limites legais, e não asseguram exclusividade. Essa relação contratual não resolve, sozinha, a proteção autoral de material puramente automatizado ou os direitos de terceiros. A revisão não foi usada para declarar exclusividade sobre todas as frases geradas. [Termos consultados](https://openai.com/policies/row-terms-of-use/).

A necessidade de divulgar assistência de IA em um manuscrito dependerá das regras do periódico e do uso efetivo. A suíte já exige preservar as declarações aplicáveis. Não foi incluída promessa de ocultação de autoria.

## Dados, plataformas e falsos positivos

A triagem automática sinalizou conteúdo de usuário ao encontrar linguagem sobre documentos e contribuições. Não foi encontrada uma implementação própria de plataforma para recebimento de manuscritos. Os alertas automáticos de política de privacidade, termos de serviço e canal de titular não foram confirmados como defeitos de uma aplicação própria.

Isso não significa ausência de tratamento pelas plataformas. GitHub, CLI e provedor do agente possuem políticas próprias. A criação futura de formulários, suporte com documentos privados, telemetria ou serviços pagos exigirá nova avaliação. [Privacidade do GitHub](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Verificação e pendências

As verificações executadas e os locais de evidência são registrados ao final deste documento. Não foram localizadas pendências de preenchimento de dados empresariais para o fluxo atual, nem foi inventado um canal privado de atendimento.

Permanecem fora do alcance: comparação textual integral com todas as fontes, auditoria dos contratos e configurações da conta do mantenedor, qualificação jurídica da contribuição humana em cada trecho, busca de marcas e análise de todas as jurisdições.

Recomenda-se avaliação por advogado antes de comercialização com garantias contratuais, redistribuição de conteúdo protegido de terceiros, recebimento de notificação ou implantação de tratamento relevante de dados pessoais. A licença padrão não afasta normas imperativas quando aplicáveis.

## Evidências e verificações locais

- Contraste calculado do texto no banner: #263b36 sobre #f3f0e8: 10.47:1; #4d5a51 sobre #f3f0e8: 6.37:1; #263b36 sobre #faf8f2: 11.23:1. Referência técnica: [WCAG 2.2, critério 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Não constitui avaliação integral de acessibilidade.
- `LICENSE:5` — trecho examinado.
- `THIRD_PARTY_NOTICES.md:13` — trecho examinado.
- `README.md:94` — trecho examinado.
- `SECURITY.md:11` — trecho examinado.
- `docs/evaluation.md:56` — trecho examinado.
- `assets/banner.svg:2` — trecho examinado.
- `scripts/validate.py:56` — trecho examinado.
- `tests/test_validation.py:45` — trecho examinado.
- Foram executados 11 testes unitários de distribuição; a verificação de licença ausente ou divergente falhou antes da implementação e passou após o ajuste.
- Foi preservada a ausência de BOM nos 14 arquivos de metadados instaláveis. As instruções dos sete módulos coincidem com a revisão examinada, exceto pela versão.
- O scanner examinou 25 arquivos textuais da cópia pública inicial; seus alertas foram triados manualmente. A extensão de análise manual incluiu os demais arquivos versionados.
