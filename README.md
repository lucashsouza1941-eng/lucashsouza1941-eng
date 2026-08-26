<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0EA5E9,100:1E3A8A&height=130&section=header"/>

# Lucas Henrique

### Full-Stack Developer · IA Aplicada a Negócios

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&pause=1200&color=38BDF8&center=true&vCenter=true&width=650&lines=Full-Stack+Developer+%7C+React+%C2%B7+Next.js+%C2%B7+Node.js;IA+Aplicada+%7C+LLMs+%C2%B7+RAG+%C2%B7+Agentes+Inteligentes;Do+discovery+ao+deploy%2C+ponta+a+ponta"/>

<br/>

[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lucashsouza.1941@gmail.com)
![Profile Views](https://komarev.com/ghpvc/?username=lucashsouza1941-eng&style=for-the-badge&color=38BDF8&label=PROFILE+VIEWS)

</div>

---

## Sobre mim

```javascript
const lucas = {
  role:      "Full-Stack Developer",
  focus:     "Aplicações web com IA integrada",
  location:  "Diadema, São Paulo — Brasil 🇧🇷",

  stack: {
    frontend: ["React", "Next.js", "TypeScript", "TailwindCSS"],
    backend:  ["Node.js", "Express", "Python", "FastAPI"],
    data:     ["PostgreSQL", "MongoDB", "Prisma", "Redis", "pgvector"],
    ai:       ["OpenAI API", "LangChain", "RAG", "Prompt Engineering"]
  },

  currently:  "Construindo agentes e assistentes RAG que rodam em produção",
  background: "8+ anos atendendo cliente antes de migrar pra tech",
  edge:       "Traduzir dor de negócio em escopo técnico viável",

  philosophy: "Código que ninguém usa não resolve problema nenhum."
};
```

> **O diferencial:** eu não entrego só a feature. Faço o discovery, entendo o processo do
> cliente, escrevo a documentação e coloco em produção. Os 8 anos em atendimento consultivo
> não são linha perdida no currículo — são o motivo de eu levantar requisito sem retrabalho.

---

## Stack

<div align="center">

<img src="https://techstack-generator.vercel.app/react-icon.svg" alt="React" width="62" height="62"/>
&nbsp;&nbsp;
<img src="https://techstack-generator.vercel.app/ts-icon.svg" alt="TypeScript" width="62" height="62"/>
&nbsp;&nbsp;
<img src="https://techstack-generator.vercel.app/js-icon.svg" alt="JavaScript" width="62" height="62"/>
&nbsp;&nbsp;
<img src="https://techstack-generator.vercel.app/python-icon.svg" alt="Python" width="62" height="62"/>
&nbsp;&nbsp;
<img src="https://techstack-generator.vercel.app/restapi-icon.svg" alt="REST API" width="62" height="62"/>
&nbsp;&nbsp;
<img src="https://techstack-generator.vercel.app/docker-icon.svg" alt="Docker" width="62" height="62"/>
&nbsp;&nbsp;
<img src="https://techstack-generator.vercel.app/github-icon.svg" alt="GitHub" width="62" height="62"/>

<br/><br/>

<img src="https://skillicons.dev/icons?i=react,nextjs,ts,nodejs,express,python,fastapi,postgres,mongodb,prisma,redis,tailwind,docker,git,vercel,postman&perline=8"/>

<br/><br/>

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

---

## Como eu integro IA numa aplicação

Não é chamada de API solta. O padrão que eu uso em produção:

```
                    ┌─────────────────────┐
   Usuário  ───────▶│   App (Next.js)     │
   WhatsApp ───────▶│   API (Node/FastAPI)│
   E-mail   ───────▶└──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │   Camada de IA      │
                    │  ┌───────────────┐  │
                    │  │ Classificação │  │  ── intenção, prioridade
                    │  ├───────────────┤  │
                    │  │   RAG         │  │  ── pgvector / embeddings
                    │  ├───────────────┤  │
                    │  │  Orquestração │  │  ── LangChain / agentes
                    │  └───────────────┘  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        PostgreSQL         Redis           Integrações
        (estado)          (cache)      (CRM, gateway, API)
```

**Na prática:** classificar antes de gerar (modelo barato filtra o caro), RAG com base
vetorizada pra resposta não alucinar, e fallback humano sempre que a confiança cai.
Log de tudo — IA em produção sem observabilidade é aposta.

---

## Projetos

<table>
<tr>
<td width="50%" valign="top">

### 💬 [Assistente RAG](https://github.com/lucashsouza1941-eng/Assistente-RAG)
`TypeScript` `OpenAI API` `pgvector`

Assistente com RAG respondendo a partir de base de conhecimento
vetorizada, com fallback para atendimento humano.

</td>
<td width="50%" valign="top">

### 🤖 [Multi-Agente — Logística](https://github.com/lucashsouza1941-eng/projeto-1-multi-agente-logistica)
`TypeScript` `LangChain` `PostgreSQL`

Orquestração de agentes de IA para triagem de e-mails, geração de
relatórios e escalonamento automático.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎨 [Portfólio](https://github.com/lucashsouza1941-eng/portfolio-lucas)
`TypeScript` `Next.js` `TailwindCSS`

Portfólio pessoal com os projetos, stack e formas de contato.

</td>
<td width="50%" valign="top">

### 🧭 [Onboarding Tour — Adalink](https://github.com/lucashsouza1941-eng/adalink-onboarding-tour)
`HTML` `JavaScript`

Tour interativo de onboarding da plataforma Adalink (Adaflow),
protótipo em HTML único.

</td>
</tr>
</table>

---

## GitHub

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=lucashsouza1941-eng&theme=tokyonight" height="200"/>
<img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=lucashsouza1941-eng&theme=tokyonight" height="200"/>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/lucashsouza1941-eng/lucashsouza1941-eng/output/snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/lucashsouza1941-eng/lucashsouza1941-eng/output/snake.svg"/>
  <img alt="Snake - grafico de contribuicoes" src="https://raw.githubusercontent.com/lucashsouza1941-eng/lucashsouza1941-eng/output/snake.svg"/>
</picture>

</div>

---

## Como eu trabalho

| | |
|---|---|
| **Discovery primeiro** | Entender o processo antes de escrever a primeira linha |
| **Documentação junto** | README, decisões e trade-offs escritos enquanto o código nasce |
| **Entrega ponta a ponta** | Do banco ao deploy — não paro na feature |
| **Valor mensurável** | Se não reduz tempo, custo ou erro, é enfeite |

---

<div align="center">

### Aberto a oportunidades Full-Stack e projetos de IA aplicada

[![Email](https://img.shields.io/badge/lucashsouza.1941@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:lucashsouza.1941@gmail.com)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0EA5E9,100:1E3A8A&height=120&section=footer"/>

</div>
