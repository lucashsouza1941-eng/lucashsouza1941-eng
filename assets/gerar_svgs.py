"""Gera os SVGs animados do README do perfil (pasta assets/).

Rodar: python assets/gerar_svgs.py
"""
import math
import random
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent  # este arquivo fica dentro de assets/
OUT.mkdir(exist_ok=True)

FONT = "'Segoe UI', Inter, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'Fira Code', Consolas, 'Courier New', monospace"
SKY = "#38BDF8"
SKY2 = "#0EA5E9"
NAVY = "#1E3A8A"
BG = "#0b1020"


def write(name, svg):
    (OUT / name).write_text(svg, encoding="utf-8")
    print("ok", name)


# ---------------------------------------------------------------- header
def header():
    w, h = 1000, 280
    rnd = random.Random(7)
    # rede neural à direita e à esquerda (fica atrás do texto, com pouca opacidade no centro)
    nodes = []
    for _ in range(34):
        x = rnd.uniform(20, w - 20)
        y = rnd.uniform(20, h - 20)
        nodes.append((x, y))
    edges = []
    for i, (x1, y1) in enumerate(nodes):
        dists = sorted(
            ((math.hypot(x1 - x2, y1 - y2), j) for j, (x2, y2) in enumerate(nodes) if j != i)
        )
        for d, j in dists[:2]:
            if i < j and d < 230:
                edges.append((i, j))

    def center_fade(x):
        # nós perto do centro (onde está o texto) ficam mais apagados
        return 0.25 + 0.75 * min(1, abs(x - w / 2) / 330)

    lines = []
    for k, (i, j) in enumerate(edges):
        (x1, y1), (x2, y2) = nodes[i], nodes[j]
        op = 0.22 * min(center_fade(x1), center_fade(x2))
        lines.append(
            f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{SKY}" stroke-opacity="{op:.2f}" stroke-width="1"/>'
        )
    # pulsos de sinal correndo por algumas arestas
    pulses = []
    for k, (i, j) in enumerate(edges[::3]):
        (x1, y1), (x2, y2) = nodes[i], nodes[j]
        dur = rnd.uniform(2.2, 4.5)
        begin = rnd.uniform(0, 3)
        pulses.append(
            f'<circle r="2.2" fill="{SKY}" filter="url(#glow)">'
            f'<animateMotion dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite" path="M{x1:.0f},{y1:.0f} L{x2:.0f},{y2:.0f}"/>'
            f'<animate attributeName="opacity" values="0;1;1;0" dur="{dur:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite"/>'
            f"</circle>"
        )
    dots = []
    for k, (x, y) in enumerate(nodes):
        f = center_fade(x)
        r = rnd.uniform(2, 3.6)
        d = rnd.uniform(1.8, 3.6)
        dots.append(
            f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="{SKY}" fill-opacity="{0.8 * f:.2f}">'
            f'<animate attributeName="r" values="{r:.1f};{r * 1.7:.1f};{r:.1f}" dur="{d:.1f}s" repeatCount="indefinite"/>'
            f'<animate attributeName="fill-opacity" values="{0.8 * f:.2f};{0.25 * f:.2f};{0.8 * f:.2f}" dur="{d:.1f}s" repeatCount="indefinite"/>'
            f"</circle>"
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0a0f1f"/>
      <stop offset="1" stop-color="#0d1117"/>
    </linearGradient>
    <radialGradient id="halo" cx="50%" cy="45%" r="55%">
      <stop offset="0" stop-color="{SKY2}" stop-opacity="0.28"/>
      <stop offset="1" stop-color="{SKY2}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox">
      <stop offset="0" stop-color="#e0f2fe"/>
      <stop offset="0.45" stop-color="#e0f2fe"/>
      <stop offset="0.5" stop-color="{SKY}"/>
      <stop offset="0.55" stop-color="#e0f2fe"/>
      <stop offset="1" stop-color="#e0f2fe"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="4s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{NAVY}"/>
      <stop offset="0.5" stop-color="{SKY}"/>
      <stop offset="1" stop-color="{NAVY}"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="-1 0;1 0" dur="3s" repeatCount="indefinite"/>
    </linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="round"><rect width="{w}" height="{h}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#round)">
    <rect width="{w}" height="{h}" fill="url(#bg)"/>
    <rect width="{w}" height="{h}" fill="url(#halo)">
      <animate attributeName="opacity" values="0.7;1;0.7" dur="5s" repeatCount="indefinite"/>
    </rect>
    {''.join(lines)}
    {''.join(dots)}
    {''.join(pulses)}
    <rect y="{h - 4}" width="{w}" height="4" fill="url(#bar)"/>
  </g>
  <text x="{w / 2}" y="112" text-anchor="middle" font-family="{FONT}" font-size="54" font-weight="800" fill="url(#shine)" letter-spacing="1">Lucas Henrique</text>
  <text x="{w / 2}" y="156" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="600" fill="{SKY}">Full-Stack Developer · IA Aplicada a Negócios</text>
  <g font-family="{MONO}" font-size="14" fill="#94a3b8" text-anchor="middle">
    <text x="{w / 2}" y="196">Diadema · São Paulo — Brasil</text>
  </g>
  <g transform="translate({w / 2 - 92},218)">
    <rect width="184" height="28" rx="14" fill="#052e1b" stroke="#22c55e" stroke-opacity="0.6"/>
    <circle cx="20" cy="14" r="5" fill="#22c55e">
      <animate attributeName="opacity" values="1;0.25;1" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="20" cy="14" r="5" fill="none" stroke="#22c55e">
      <animate attributeName="r" values="5;11" dur="1.6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <text x="102" y="19" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="600" fill="#86efac">aberto a oportunidades</text>
  </g>
</svg>"""
    write("header.svg", svg)


# ---------------------------------------------------------------- fluxo de IA
def fluxo():
    w, h = 1000, 380

    def box(x, y, bw, bh, label, sub=None, stroke=SKY, fill="#0f172a", fs=15):
        s = f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="10" fill="{fill}" stroke="{stroke}" stroke-opacity="0.55"/>'
        ty = y + bh / 2 + (5 if not sub else -2)
        s += f'<text x="{x + bw / 2}" y="{ty}" text-anchor="middle" font-family="{FONT}" font-size="{fs}" font-weight="600" fill="#e2e8f0">{escape(label)}</text>'
        if sub:
            s += f'<text x="{x + bw / 2}" y="{ty + 18}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#94a3b8">{escape(sub)}</text>'
        return s

    def flow(path, dur, begin=0.0, color=SKY):
        return (
            f'<path d="{path}" fill="none" stroke="#334155" stroke-width="2"/>'
            f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="6 14" stroke-linecap="round">'
            f'<animate attributeName="stroke-dashoffset" values="40;0" dur="0.9s" repeatCount="indefinite"/></path>'
            f'<circle r="4" fill="{color}" filter="url(#g)"><animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" path="{path}"/></circle>'
        )

    parts = []
    # entradas
    ins = [("Usuário · App", 60), ("WhatsApp", 130), ("E-mail", 200)]
    for i, (lab, y) in enumerate(ins):
        parts.append(box(20, y, 150, 44, lab))
        parts.append(flow(f"M170,{y + 22} C215,{y + 22} 215,152 250,152", 2.2, i * 0.5))
    # API
    parts.append(box(250, 110, 160, 84, "API", "Next.js · Node · FastAPI"))
    parts.append(flow("M410,152 L470,152", 1.4))
    # camada de IA
    parts.append(
        f'<rect x="470" y="30" width="260" height="244" rx="14" fill="#0b1328" stroke="url(#ring)" stroke-width="2"/>'
        f'<text x="600" y="58" text-anchor="middle" font-family="{FONT}" font-size="15" font-weight="700" fill="{SKY}">Camada de IA</text>'
    )
    steps = [
        ("1 · Classificação", "modelo barato filtra o caro"),
        ("2 · RAG", "pgvector · embeddings"),
        ("3 · Orquestração", "agentes · ferramentas"),
    ]
    for i, (a, b) in enumerate(steps):
        y = 74 + i * 64
        parts.append(
            f'<rect x="490" y="{y}" width="220" height="52" rx="9" fill="#0f172a" stroke="#1e293b">'
            f'<animate attributeName="stroke" values="#1e293b;{SKY};#1e293b;#1e293b" keyTimes="0;0.15;0.33;1" dur="3s" begin="{i}s" repeatCount="indefinite"/></rect>'
            f'<text x="600" y="{y + 22}" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="600" fill="#e2e8f0">{escape(a)}</text>'
            f'<text x="600" y="{y + 40}" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#94a3b8">{escape(b)}</text>'
        )
    # saídas
    outs = [("PostgreSQL", "estado", 40), ("Redis", "cache", 128), ("Integrações", "CRM · gateway · API", 216)]
    for i, (a, b, y) in enumerate(outs):
        parts.append(flow(f"M730,152 C770,152 770,{y + 26} 800,{y + 26}", 2.2, i * 0.6))
        parts.append(box(800, y, 180, 52, a, b))
    # rodapé: guardrails
    chips = [("fallback humano", "#f59e0b"), ("log de tudo", "#22c55e"), ("custo sob controle", SKY)]
    x = 250
    for lab, c in chips:
        cw = 22 + len(lab) * 8
        parts.append(
            f'<g transform="translate({x},318)"><rect width="{cw}" height="30" rx="15" fill="none" stroke="{c}" stroke-opacity="0.7"/>'
            f'<circle cx="15" cy="15" r="4" fill="{c}"><animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/></circle>'
            f'<text x="{cw / 2 + 6}" y="20" text-anchor="middle" font-family="{FONT}" font-size="13" fill="#cbd5e1">{lab}</text></g>'
        )
        x += cw + 24

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <filter id="g" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{SKY}"/><stop offset="0.5" stop-color="{NAVY}"/><stop offset="1" stop-color="{SKY}"/>
      <animateTransform attributeName="gradientTransform" type="rotate" values="0 .5 .5;360 .5 .5" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" rx="18" fill="{BG}"/>
  {''.join(parts)}
</svg>"""
    write("fluxo-ia.svg", svg)


# ---------------------------------------------------------------- cards de projeto
PROJETOS = [
    ("orion", "🧠", "ORION", "Privado", "#a78bfa",
     ["Assistente de IA pessoal self-hosted, rodando 24/7:",
      "chat que executa ferramentas, rotinas agendadas,",
      "memória persistente com RAG e cópia diária."],
     ["Node.js", "React", "Claude", "RAG"]),
    ("atlas", "🧭", "ATLAS", "Privado", "#a78bfa",
     ["Business OS AI-native: SaaS multi-tenant com MFA,",
      "auditoria em cadeia de hashes, outbox de eventos",
      "e módulo financeiro (fluxo de caixa, aging)."],
     ["TypeScript", "Turborepo", "Postgres", "Docker"]),
    ("dindin", "💸", "Din Din", "Privado", "#a78bfa",
     ["Finanças compartilhadas em tempo real para casa,",
      "casal ou sócios: grupos, gráficos, ritmo do mês,",
      "lista de compras e copiloto de IA."],
     ["Next.js", "Supabase", "Realtime", "Gemini"]),
    ("helaine", "✂️", "Helaine Tranças", "Cliente real", "#22c55e",
     ["Agendamento online em produção: cada serviço",
      "reserva o tempo certo, folgas, painel de admin",
      "e aviso para a profissional pelo WhatsApp."],
     ["Next.js", "Supabase", "Vercel"]),
    ("regua", "📏", "Régua de Avaliação", "Open source", SKY,
     ["Framework para avaliar saídas de LLMs: casos de",
      "teste, juízes exato / semântico / LLM, histórico",
      "de execuções e relatório em HTML."],
     ["Python", "LLM-as-judge", "CLI"]),
    ("costa", "🌍", "Instituto Costa da Mina", "Cliente real", "#22c55e",
     ["Novo site institucional de uma ONG da Cidade",
      "Ademar, Zona Sul de São Paulo: projetos,",
      "transparência e formas de apoiar."],
     ["Next.js", "TypeScript", "Tailwind"]),
]


def card(slug, icon, title, tag, tag_color, desc, techs, idx):
    w, h = 490, 210
    chips = []
    x = 22
    for t in techs:
        cw = 18 + len(t) * 7.4
        chips.append(
            f'<g transform="translate({x:.0f},168)"><rect width="{cw:.0f}" height="24" rx="12" fill="#111c33" stroke="#1e3a5f"/>'
            f'<text x="{cw / 2:.0f}" y="16.5" text-anchor="middle" font-family="{MONO}" font-size="12" fill="#bae6fd">{escape(t)}</text></g>'
        )
        x += cw + 8
    tw = 20 + len(tag) * 7.6
    lines = "".join(
        f'<text x="22" y="{96 + i * 21}" font-family="{FONT}" font-size="14.5" fill="#cbd5e1">{escape(l)}</text>'
        for i, l in enumerate(desc)
    )
    delay = idx * 0.6
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="b" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{SKY}"/><stop offset="0.35" stop-color="#1e293b"/><stop offset="0.65" stop-color="#1e293b"/><stop offset="1" stop-color="{NAVY}"/>
      <animateTransform attributeName="gradientTransform" type="rotate" values="0 .5 .5;360 .5 .5" dur="7s" begin="-{delay}s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="c"><rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="16"/></clipPath>
  </defs>
  <rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="16" fill="{BG}" stroke="url(#b)" stroke-width="2"/>
  <g clip-path="url(#c)">
    <rect x="-200" y="0" width="160" height="{h}" fill="url(#sweep)" transform="skewX(-20)">
      <animate attributeName="x" values="-260;{w + 120}" dur="5s" begin="{delay}s" repeatCount="indefinite"/>
    </rect>
  </g>
  <text x="22" y="52" font-size="26">{icon}</text>
  <text x="62" y="50" font-family="{FONT}" font-size="22" font-weight="700" fill="#f1f5f9">{escape(title)}</text>
  <g transform="translate({w - tw - 20:.0f},30)">
    <rect width="{tw:.0f}" height="24" rx="12" fill="{tag_color}" fill-opacity="0.12" stroke="{tag_color}" stroke-opacity="0.6"/>
    <text x="{tw / 2:.0f}" y="16.5" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="600" fill="{tag_color}">{escape(tag)}</text>
  </g>
  <rect x="22" y="66" width="44" height="3" rx="1.5" fill="{SKY}">
    <animate attributeName="width" values="44;120;44" dur="4s" begin="{delay}s" repeatCount="indefinite"/>
  </rect>
  {lines}
  {''.join(chips)}
</svg>"""
    write(f"card-{slug}.svg", svg)


def divisor():
    w, h = 1000, 12
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs><linearGradient id="d" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{SKY}" stop-opacity="0"/><stop offset="0.5" stop-color="{SKY}"/><stop offset="1" stop-color="{SKY}" stop-opacity="0"/>
    <animateTransform attributeName="gradientTransform" type="translate" values="-0.6 0;0.6 0;-0.6 0" dur="6s" repeatCount="indefinite"/>
  </linearGradient></defs>
  <rect y="5" width="{w}" height="2" rx="1" fill="url(#d)"/>
</svg>"""
    write("divisor.svg", svg)


if __name__ == "__main__":
    header()
    fluxo()
    for i, p in enumerate(PROJETOS):
        card(*p, i)
    divisor()
