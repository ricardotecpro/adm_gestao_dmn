import os

EX_DIR = r"d:\SourceCode\REPOS\github.io\adm_gestao_dmn\docs\exercicios"

data = {
    "01": {
        "title": "Intro ao Empreendedorismo",
        "q1": "Defina o que é ser um empreendedor com suas palavras.",
        "q2": "Quais são as diferenças marcantes entre o empreendedor por necessidade e o por oportunidade?",
        "q3": "Um funcionário otimiza um setor interno reduzindo custos em 30%. Ele pode ser considerado empreendedor? Justifique baseado nos tipos de perfis.",
        "q4": "Explique a importância da característica 'Correr Riscos Calculados' na visão empreendedora.",
        "q5": "Como a mentalidade 'Lean Startup' e o uso de MVP revolucionam a validação de um empreendimento, diferenciando da abertura clássica de empresas de décadas atrás?",
        "a1": "Ser empreendedor é uma postura de encontrar soluções, criar inovações e resolver problemas gerando valor, não se resumindo apenas a abrir o próprio negócio ou CNPJ.",
        "a2": "O empreendedor por necessidade entra no mercado por falta de opção de renda (foco em sobrevivência e curto prazo). O por oportunidade observa uma lacuna no mercado e planeja seu negócio visando crescimento, lucro e inovação.",
        "a3": "Sim, esse comportamento define o 'Intraempreendedor', aquele que inova e gera resultados exponenciais atuando dentro da empresa de terceiros, como um colaborador.",
        "a4": "Mitigar o risco é essencial para não falir precocemente. Correr risco calculado não é apostar cegamente, mas usar dados e testes pequenos para confirmar as chances antes de investir pesadamente.",
        "a5": "O Lean Startup foca na agilidade. Em vez de grandes planejamentos e produções caras (que talvez o cliente não queira), cria-se um MVP (Produto Mínimo Viável) rápido e barato. A validação perante os clientes reais dita o que será realmente desenvolvido, reduzindo o custo da falha."
    },
    "02": {
        "title": "Identificação de Oportunidades",
        "q1": "Diferencie uma Ideia de uma Oportunidade real.",
        "q2": "Qual o papel das 'dores de clientes' na criação de oportunidades de negócios?",
        "q3": "De que forma o avanço tecnológico cria oportunidades para nichos até então ignorados? Dê um exemplo.",
        "q4": "Descreva como a segmentação ajuda a validar e penetrar no mercado com mais precisão.",
        "q5": "Construa uma Matriz CSD para a ideia de um 'Aplicativo de Lavagem de Carros a Seco em Domicílio' e explique a estratégia de buscar o Oceano Azul para esse mercado.",
        "a1": "A ideia é algo abstrato e criativo (o 'seria legal fazer'). Uma oportunidade é uma ideia que já encontrou viabilidade econômica e que o mercado tem demanda comprovada para consumir.",
        "a2": "As dores apontam fricções (problemas e estresses) na jornada do usuário. Onde há uma dor real e incômoda, há espaço para soluções pagas. Uma dor não resolvida é a maior propulsora de um novo negócio.",
        "a3": "O avanço gera democratização e redução de custos operacionais. Exemplo: impressoras 3D permitem a pequenos empreendedores criar soluções customizadas plásticas (peças de reposição) que antes exigiriam fabricação em massa em grandes indústrias.",
        "a4": "A segmentação impede que o empreendedor 'tente vender para todo mundo e não venda para ninguém'. Focar num nicho cria comunicação mais assertiva, diminuindo custo de atração e fidelizando os primeiros usuários mais rapidamente.",
        "a5": "Matriz CSD - Certezas (ex: clientes gostam do carro limpo), Suposições (ex: clientes estão dispostos a pagar um pequeno adicional pela conveniência em casa) e Dúvidas (ex: os condomínios permitirão a entrada dos lavadores?). O Oceano Azul consistiria em focar num público ou num adicional ecológico desatendido pelas lavagens tradicionais, escapando da guerra predatória de preços da lavagem física no posto."
    },
    "03": {
        "title": "Análise de Valor",
        "q1": "O que significa 'Percepção de Valor' pelo cliente?",
        "q2": "Qual é a relação entre preço, custo e valor na confecção de um produto?",
        "q3": "Se uma empresa inova mas o cliente não percebe melhoria na usabilidade, houve entrega de valor? Por quê?",
        "q4": "Apresente os três pilares que sustentam uma Proposta de Valor imbatível.",
        "q5": "Explique a dinâmica do CAC e do LTV. Demonstre matematicamente por que um negócio cujo LTV seja 3x maior que o CAC tem uma análise de valor robusta.",
        "a1": "É o quanto o cliente percebe de benefício intangível ou prático que o produto proporciona em relação ao esforço empregado (seja dinheiro, tempo ou frustração) para obtê-lo.",
        "a2": "Custo é o gasto real para produzir aquilo. Preço é o valor monetário de venda exigido. Valor é a representação do quanto aquele bem ou serviço transforma a vida do usuário, justificando e geralmente ultrapassando muito o preço e o custo.",
        "a3": "Não houve. A inovação que não gera benefício percebido pelo usuário é apenas uma 'invenção' tecnológica irrelevante mercadologicamente, pois o valor é estritamente ditado pelo olhar e pela resolução do problema do cliente.",
        "a4": "Aliviar dores (diminuir trabalhos ruins e frustrações), criar ganhos (gerar resultados positivos esperados ou inesperados) e o ajuste problema/solução, formatados em produtos que encapsulem isso.",
        "a5": "CAC (Custo de Aquisição de Cliente) é quanto o marketing gasta para atrair um cliente pagante. LTV (Lifetime Value) é todo o lucro gerado por aquele cliente o tempo que ele for seu usuário. Se LTV = R$300 e CAC = R$100, a relação >3x significa que a empresa não sangra capital. O valor retido do usuário financia com sobras as aquisições futuras, permitindo escala tracionada."
    },
    "04": {
        "title": "Processo de Inovação",
        "q1": "Quais são as diferenças conceituais entre Inovação Incremental e Inovação Disruptiva?",
        "q2": "Defina sustentabilidade na inovação. Por que inovar é vital para a longevidade?",
        "q3": "Inovar sempre significa criar tecnologia do zero? Forneça um exemplo base.",
        "q4": "De que maneiras a Cultura Organizacional afeta as taxas de inovação na empresa?",
        "q5": "Dado o nível de TRL (Technology Readiness Level), descreva como a inovação flui do ambiente acadêmico até o teste validado, e o que é o 'Vale da Morte' da Inovação neste percurso.",
        "a1": "Inovação Incremental foca na melhoria contínua e paulatina do que já existe (ex: um carro mais leve). Inovação Disruptiva quebra a cadeia de paradigmas estabelecidos, revolucionando e às vezes aniquilando os antigos mercados (ex: Netflix destruindo locadoras físicas).",
        "a2": "Inovação sustentável é prezar para que a empresa possa sempre se adequar às exigências vigentes para nunca tornar-se obsoleta. Produtos têm ciclos de morte e declínio curtos na era moderna, exigindo pivotagem ou obsolescência programada planejadas.",
        "a3": "Não. Às vezes a inovação é em Processo, em Modelo de Negócio ou Experiência de Usuário. O modelo de assinatura de livros não cria uma 'tecnologia' vitalmente nova, mas readapta o processo de entrega e recebimento.",
        "a4": "Culturas rígidas e que punem falhas duramente extirpam a iniciativa, matando inovações e ideias experimentais. Uma cultura de inovação demanda dar segurança psicológica para testes, iterando baseada em fatos e não em burocracia departamental inibidora.",
        "a5": "O processo começa na maturidade tecnológica nivelada em ciência básica (TRL 1) até protótipos comprovados (TRL 9). O 'Vale da Morte' (Death Valley of Innovation) descreve a lacuna letal (geralmente do TRL 4 a 6) onde projetos nascidos da academia perdem financiamento ou apoio, morrendo antes que a ideia prove-se economicamente para virar efetivamente um produto massificado."
    },
    "05": {
        "title": "Estratégias e Ideação",
        "q1": "Qual a finalidade de realizar uma sessão de Brainstorming focada?",
        "q2": "O Design Thinking coloca o humano no centro. O que isso significa na prática da ideação?",
        "q3": "Como o processo de divergência (criar escolhas) e convergência (fazer escolhas) estrutura as dinâmicas?",
        "q4": "Cite dois mitigadores importantes na estratégia visual ou mind-mapping para resolução.",
        "q5": "Descreva o modelo do 'Duplo Diamante' no contexto avançado e discuta como focar no Espaço do Problema é diferencial antes de pular para o Espaço da Solução.",
        "a1": "É uma tempestade de ideias cujo objetivo é inicialmente abolir qualquer autocrítica, trazendo quantidade bruta de premissas sobre as quais os blocos refinados e inovadores mais factíveis podem brotar depois.",
        "a2": "Significa inovar e desenhar processos sempre baseados em Empatia perante o usuário final. Desenvolver as soluções calçando os sapatos dele, para depois casar essas ideias com a viabilidade tecnológica e mercadológica cabíveis.",
        "a3": "A ideação pura é caótica. Usa-se a divergência amplamente primeiro para abrir caminhos, então se impõe matrizes (ex: Impacto x Esforço) operando a Convergência de forma seletiva para focar o capital nos esforços vencedores.",
        "a4": "O mind-mapping ajuda associando visual e radialmente os problemas correlacionados. Mitigadores ajudam pois destivam 'travas mentais' do cérebro linear das planilhas, operando sob associações cognitivas sinápticas soltas.",
        "a5": "O Duplo Diamante tem duas partes: 1) Descobrir e Definir (O Primeiro Diamante); 2) Desenhar e Entregar (O Segundo Diamante). A maioria falha ao pular ao Espaço da Solução. Disputar e mergulhar em definições precisas sobre a verdadeira dor subjacente (Espaço do Problema) evita gastar energia excelente na solução perfeita da doença totalmente equivocada."
    },
    "06": {
        "title": "Plano de Negócios",
        "q1": "Por que estruturamos um Plano de Negócios clássico perante investidores bancários?",
        "q2": "Destaque os principais componentes do Sumário Executivo.",
        "q3": "Como validar uma Projeção de Caixa sem conhecer o futuro? Que medidas usar?",
        "q4": "O Plano Operacional ajuda a prever a logística, os insumos essenciais e a real viabilidade do esforço. Qual a essência fundamental nele?",
        "q5": "Para modelos ágeis em incerteza, como conciliar o Plano de Negócios Tradicional com a análise de Break-Even dinâmico em cenários desfavoráveis e incertos? Justifique em relação ao cálculo de OPEX e fixos contínuos.",
        "a1": "Modelos como bancos tradicionais ainda não toleram total abstenção ou matrizes ágeis puras de empreendedorismo para aportes volumosos; necessitam de histórico formal, previsão plurianual de receitas, garantias reais e plano mercadológico burocratizado estrutural.",
        "a2": "É o resumo com foco na dor, a solução, mercado endereçável, vantagem competitiva e projeção da lucratividade ou margem de operação visando atrair interesse imediato a leitura minuciosa posterior.",
        "a3": "Criando 3 cenários de variância: Cenario Otimista, Cenario Base, Cenario Pessimista (Conservador). Projetos sensatos operam seu planejamento pelo olhar Base, mas provisionam recursos blindados garantindo que nem em caso do Pessimista, a operação feche antes de pivotar.",
        "a4": "Determinar qual capacidade real instalada o negócio precisa. Ele mitiga riscos traduzindo os layouts de instalação das máquinas, horários dos colaboradores ou dependências de entrega da Nuvem antes que o gargalo sufoque.",
        "a5": "Em startups flexíveis as variáveis mudam rapidamente e um Plano anual é ultrapassado em dias reais; mas a premissa de Break-even (Lucro Zero) é contínua. Conciliar significa injetar reavaliações trimestrais dos KPIs num Plano Ágil. O empreendedor deve modular a taxa OPEX (Despesas Mensais de Operação como cloud flexível ou pessoal subcontratado), permitindo que a variação e flexibilização garanta a descida do Break-even pontual mesmo nas adversidades temporárias de receitas falhas."
    },
    "07": {
        "title": "Modelagem Canvas",
        "q1": "Qual a grande diferença e grande proposta revolucionária do Canvas sobre o Plano clássico (Seapa/Sebrae)?",
        "q2": "Quantos e quais são os blocos lógicos essenciais do Business Model Canvas (BMC)?",
        "q3": "Se uma alteração radical for feita na Segmentação de Clientes, que blocos do Canvas sofreriam abalo em cadeia direto?",
        "q4": "Descreva o papel lógico e semântico dos Canais versus a área de Relacionamento no Canvas.",
        "q5": "O Canvas não é estático. Use o conceito de Padronização e Business Model Patterns, aplique isso definindo a configuração atípica de um Business Canvas na vertente Freemium Digital e Long Tail de produtos físicos nichados.",
        "a1": "A representação tática imediata, holística e relacional do funcionamento orgânico da empresa focado inteiramente na geração, estruturação e percepção de valor. A visualização única cabe numa folha visual onde correlações são intercedidas em tempo real nas brainstormings co-criadas e colaboradas visualmente.",
        "a2": "9 blocos fundamentais: Segmentação de Clientes, Proposta de Valor, Canais, Relacionamento, Fontes de Receita, Recursos Chave, Atividades Chave, Parceiros Chave, e Estrutura de Custo.",
        "a3": "A Proposta de Valor fatalmente (o encaixe que os liga), além do Relacionamento que dita a personalização deste novo usuário alvo, dos Canais necessários para atingi-lo e possivelmente nas Fontes de Receitas atreladas a cobrança tolerada deste novo alvo.",
        "a4": "Canais descrevem APENAS ONDE os clientes obtêm o valor (a via tangível: lojistas virtuais, carreta de entrega). Relacionamento dita o 'COMO' é cultivado e mantido na base o suporte cognitivo e interações que engajam esse usuário permanentemente (retenção).",
        "a5": "O Modelo Freemium anota o bloco Segmentação dividido estruturalmente entre Massa Gratuita vs Nicho Premium com a área Fontes de Receita focada em zero R$ para a vasta esmagadora fatia dependendo totalmente da pequena porcentagem pagante que tem blocos de Custos diluídos. No padrão Long Tail, a Proposta de Valor prega vastidão seletiva, Segmentação de inúmeros pequenos grupos e Recursos-Chave calcados unicamente numa Cadeia Logística infalível que entregue diversificação minúscula perene com lucro na agregação massiva das pequenezas de demandas cauda longa marginalizadas pelas vendedoras convencionais restritas aos Mainstreams blockbusters monopolistas."
    },
    "08": {
        "title": "Segmentação de Clientes",
        "q1": "O que significa nichar um mercado e as vantagens desta restrição?",
        "q2": "Tratar características demográficas sozinhas atesta resultados plenos para startups? Por quê? ",
        "q3": "Construa e diferencie a essência de Público-alvo versus da Persona Analítica Ideal.",
        "q4": "Exemplifique B2B e B2C determinando quem efetua a ação vital de compra corporativa.",
        "q5": "O framework Intermediário 'Job To Be Done (JTBD)' inverte as lógicas do marketing e as personas engessadas e cegas faturadas globalmente pelo sistema demográfico. Desenvolva através da explicação com uma furadeira qual seria na realidade a tarefa subjacente.",
        "a1": "É a exclusão e limitação consciente e minuciosa focalizada perante pequenos grupos de hábitos correlatos fortíssimos com carências latentes onde pouca e negligenciada concorrência de tubarões do negócio atuam, diminuindo gastos e aumentando conversão monopolista isolada.",
        "a2": "Demografia avisa o corpo, mas cala sob os comportamentos. Um perfil demográfico (Homem, rico, londrino e solteiro da realeza) agruparia Príncipe Charles com o RockStar excêntrico Ozzie. Ambos consumem mundos em oposição diametral perigosa, fazendo de campanhas puramente de 'Faixa' uma miríade vazia sem gatilhos.",
        "a3": "Público-alvo generaliza ('homens de 35 anos casados querendo roupas sociais para frio'). A Persona refina em uma bio tangível que mimetiza comportamentais reais: ('Roberto, analista estressado que viaja de ponte aérea e detesta camisas que amassam da viagem necessitando sempre da estética perante o CEO sem ir pra tabua de passar ou lavar o terno todo momento no saguão').",
        "a4": "B2C vende a nós pontualmente (mercado para casa, cinema físico familiar). B2B se destina a relações perenes escaláveis onde uma empresa dita compras complexas e decisivas por fluxos rigorosos (Microsoft contratando SAP para contabilidade inteira da sua frota).",
        "a5": "As pessoas não ligam à métrica ou brocas das furadeiras; compram furadeiras por desejar desesperadamente os Furos das Paredes e ultimamente quadros ou memórias presas alí. O JTBD dita a contratação da circunstância do Progresso onde os usuários pagariam até fitas da 3M dupla-face para sanar o 'Colar Recordação Afetiva Evocada'. Produto engessado fali. Progresso contratado pelo Consumidor ganha LTV."
    }
}

# The remaining 8 lessons
data2 = {
    "09": {
        "title": "Proposta de Valor",
        "q1": "Defina Proposta de Valor.",
        "q2": "O Valor sempre deve girar em torno apenas de vantagens tangíveis das especificações métricas? Justifique no design.",
        "q3": "Um diferencial muito fácil de ser copiado pela vasta concorrência assegura sustentabilidade da Proposta ao tempo? Explique com métricas simples.",
        "q4": "Como inovar perante mercados hiper superlotados provando que a Promessa Mútua de Valor perdura.",
        "q5": "Utilizando o framework Value Proposition Canvas na complexidade intermediária dita acima do Value Proposition Canvas (VPC), descreva como Aliviadores da Dor e os Ganhadores criam correspondência fatal perante dores agudas, explicando a barreira e o 'FIT problem-solution'.",
        "a1": "É a declaração objetiva global da promessa feita e entregada pela organização indicando e ratificando categoricamente motivos lógicos indiscutíveis perante a conversão e uso final.",
        "a2": "Tangível é facilmente derrubável e quantitativo. Falar possuo 8K RAM não fideliza e entra no desuso ou obsolescência imediata. O Intangível remanesce para a vida e confere sentido vital perante uso cognitivo das marcas agregadoras atrativas onde status confere relevo.",
        "a3": "Não assegura e rui o negócio. É uma Vantagem Transitória e de ciclo de sobrevida pífia onde apenas gera o efeito do 'grosseiro balcão do dumping mercenário agressivo' matando inovações das outras na precificação e zerando fluxos. Valor demanda Defensibilidade real das barreiras de entrada (ecossistemas pesados ou patentes imunes a clonagens laterais e falsificações contínuas).",
        "a4": "Sublinhando propostas segmentadas altamente em Océanos Azuis das vertentes ignoradas ou aprimorando interfaces UX de onde dores negligenciadas por monopolistas agigantados não conseguem focar, provando agilidade imbatível e customizando relações ao topo de atendimento humano que mega cooperativas esmagam com SACs robóticos inúteis.",
        "a5": "Não fabricamos um pneu por fabricar. O FIT no Value Proposition Canvas engata e colide diametralmente uma dor fortíssima atestada clinicamente no lado direito em encaixes com Pílulas ou Criadores absolutos do alívio desta fricção específica modelado no Pneu RunFlat ou que se enche com espuma em buracos não interrompendo viagens solitárias fatais das estradas sem frotas, gerando FIT problemático e Produto Perfeito."
    },
    "10": {
        "title": "Canais de Comunicação",
        "q1": "O que definem os Canais de forma teórica em relação orgânica às vendas no modelo lido?",
        "q2": "Canal primariamente tem apenas e unicamente intuito de venda transacional? Cite um contraponto do marketing.",
        "q3": "Qual a disparidade de viabilidade e de impacto comparando canais Diretos com canais Indiretos parceirizados.",
        "q4": "Defina o viés moderno entre atuar num Multicanal perante um Omnichannel onde marcas modernas aportam.",
        "q5": "Canais se comunicam matematicamente de forma contígua a taxas de funil perante CAC. Demonstre o racional intermediário estratégico que fundamenta em cancelar certas bases para manter a taxa de conversão final escalável nas estratégias focadas do Omnichannel.",
        "a1": "Constituem canais como todos os meios tangíveis essenciais que as empresas elegem focar para comunicação e tangibilização na entrega da Venda ou Proposta exata do final dos processos interativos mercantis engajadores com Usuários Alvos puros e definidos no seu Bloco de Clientes.",
        "a2": "Jamais. São engrenagens complexas também dotadas do poder vital de Suporte no pós-vendas engajado, comunicação unilateral e bilateral nos diálogos analíticos de feedback interativos na comunidade engajadora e entrega perene (Delivery do intangível Cloud por exemplos ativados continuados aos assinantes).",
        "a3": "Venda Própria via E-commerce Direto permite reter a margem cheia sem divisórias pesadas atestadas para parceiros, no entanto, captação é restrita e lenta na tração. Ingressar via canal Parceiro Indireto perante Gigantes capilariza seu horizonte em 200 vezes mais escala do dia a noite espalhando os produtos ativamente na margem onde o lucro cortado reflete uma compensação pelo tráfego passivo gigante trazido nas prateleiras dos tubarões em rede atestada em ecossistemas de terceiros e comissionados diretos.",
        "a4": "Multicanal dispõe todos os canais perante a base de clientes, desmembradamente sem integrações fluidas onde dados truncam ou experiências rompem-se de telas e físicos. O Omnichannel entrelaça em um cordão bi-sistêmico onde a intersecção de uso se perpetua harmoniosamente no físico para site, do site as notificações mobile e das notificações às retiradas na Loja nativa do bairro sem dor gerando um Super Ecossistema atrelado focado.",
        "a5": "O funil determina o viés exato no gargalo. Um empreendedor intermediário rastreia UTMs de canais onde gasta e perfura tráfego digital inerte, se um canal acarreta com Clics astronômicos massivos (vaidade de branding pura) porem a base Conversiva lá no check-out se esfria perto do traço fatal, o CAC engole lucros vitais, devendo assim ser aniquilado de verba redirecionando verbas otimizadas ao nicho onde Clientes ideiais operam com menor abandono convertidos nos ecossistemas vitais da escala das Retenções perenes absolutas ou do lucro líquido massificado otimamente viabilizado a aquisição e fechamentos transacionais garantidos a curtíssimo período em caixas da base central."
    },
    "11": {
        "title": "Relacionamento com Cliente",
        "q1": "Como é percebida uma relação Autoatendimento e que benefício tem para startups iniciais do cenário SAAS?",
        "q2": "No extremo adverso, para mercados Ultra High Tickets ou B2B Complexos que relacionamento se opera?",
        "q3": "A cocriação vem a fortalecer bases. Exemplifique cocriações.",
        "q4": "Fidelidade e Retenção custam muito mais do que Captação agressiva? Expresse o racional comum vital do Marketing.",
        "q5": "No nível profundo analítico como Cohort Analysis e a mensuração ativa de Churn Rate (Evasões) protegem os ativos contábeis antes das falências irrevesíveis dos Modelos de Negócios e qual atuação é empregada por analistas CS (Customer Success) e Onboardings baseados nas matrizes do software de relacionamento reativo intermediário SaaS.",
        "a1": "Trata-se do zero suporte direto humano. Beneficia margem total e atende massificações exponenciais globais do produto SaaS propiciando FAQ avançadas e fluxos fluídos intuitivos onde um em trilhares se depara a ticket humano, garantindo altíssimo escalonamento sem travamentos físicos e de turnos nos callcenters vitais locais de custeio base altíssimo.",
        "a2": "Operam no oposto total com o Relacionamento via Assistência Pessoal Dedicada em que o Gestor Pleno e Diretor intercedem contas diretas, viajam e participam ativamente da instalação nas engrenagens das mega corporações prestando curadoria infalível baseados na alta retenção e lucros colossais das faturas recorrentes da exclusividade do consultivo vital das implantações vitais longas engessadas corporativas macro ambientais do ecossistema contratado do projeto.",
        "a3": "Membros criados de comunidades vitais do YouTube participando beta-testing as vertentes do hardware que amam ativamente apontando soluções colaborativamente (Ex. Testadores Insiders influentes do software), engajando o consumidor como braço proativo das invenções plenas perante a empresa de base matricial que eles cultuam e reverenciam como adeptos das marcas vitais globais consagradas.",
        "a4": "Custa brutalmente o oposto! Adquirir cliente novo custa estatisticamente entre 5 a 7 vezes muito mais esforço no funil de Ads agressivo e convencimentos transpondo inércias brutais do que reter o próprio leal da base atual ou fazer upselling nele engajando sua rotatividade constante num ciclo infinito sem custo atrelado do zero para aquisição de atenção em mídias dispersíveis perante barulheiras do concorrente feroz da internet moderna atual ou mídias físicas saturadas mundiais engessadas.",
        "a5": "Medir a mortalidade (Churn) não devolve mortos, por isso as Cohorts atuam lógicas preditivas. Rastreia-se as Turmas de Datas Específicas atestando qual fase interativa dita fadigas e falhas de retenção. Sucessores e CS atuam no diagnóstico preventivo intercedendo automações (Aulas vitais tutoriais no Onboarding guiado aos usuários inativos ou estagnados nas fases sensíveis cruciais) antes do bloqueio total e evasões colossais catastróficas. A premissa central de saúde da startup e da LTV se consagra através da proatividade atrelada aos alertas da base dos cohorts."
    },
    "12": {
        "title": "Atividades-chave",
        "q1": "Resuma a premissa de que o modelo de negócio baseia e direciona o foco do Empreendedor e não as macro gerências irrelevantes.",
        "q2": "Qual seria uma Atividade-chave focada em startups puras de software versus logística atestadas?",
        "q3": "Como as atividades principais protegem o núcleo da corporação perante concorrentes que agem focados lateralmente.",
        "q4": "Defina plataforma ativa e Resolução de dores interligadas a um núcleo matricial de serviço corporativo consultivo ativo vital nos fluxos diários gerenciais propostos no mercado global ativo do Canvas padrão ideal testado e validado e escalonado interativamente na gestão do time matricial base ativa do mercado corporativo clássico vital pleno moderno no cenário global atual.",
        "q5": "Elucide na profundidade da Teoria das Restrições (TOC) explanando gargalos orgânicos e justifique por que 'Otimizar um setor ou atividades irrelevante só prejudica as ineficiências latentes do modelo' perante um núcleo produtivo empresarial que subordina perdas.",
        "a1": "A empresa não existe para \"Bater Ponto burocrático\", atrelam e existem ao propósito direto único exclusivo orgânico que move suas entregas prometidas às dores. A Apple existe para inovar engenharia vital estética da base orgânica. Uber para gerir servidores do algoritmo em escala mundial real.",
        "a2": "Na startup focada e programada em SAAS o núcleo vital reside base em Codificação plena ativa, sustentabilidade das rotinas lógicas no servidor vital e Design base de Software perante os Cloud Engines ativos. Em distribuidão logística e marketplace atestada (Mercado Livre em base) o núcleo se direciona ativamente perante malhas atestadas de transporte modal interligado logístico atrelado pleno em galpões com CD ativo logístico fluído das esteiras de base matricial operacional.",
        "a3": "Sustentam porque não se atrelam ou não desviam a mira gastando milhões ou atenção dispersível inútil do CEO base com tarefas administrativas contábeis perenes simples triviais rotineiras (essas são atestadas e viabilizadas pela terceirização passiva plena corporativa). Todo pingo vital se convergia na Propriedade de núcleo duro em barreiras da entrada imbuídas num conhecimento que NENHUM player de fora consegue mimetizar num mês de plágio.",
        "a4": "Plataforma ativa gere e aprimora interligamento como nos Marketplaces (Uber app interativo com motoristas logados sem quedas brutais globais gerando rotas do algoritmo atrelado em segundos vitais lógicos). Resolvedor atua com foco do núcleo em Desafio como hospitais de alto patamar solucionando cirurgias vitais da complexidade atestada médica ou advogados corporativos prestando lógicas resolutivas jurídicas da intersecção processual atrelada ativamente engenhada nos fóruns atestadamente perenes da nação.",
        "a5": "O elo dita o poder atrelado de rebentamento de corrente onde o peso de toda a vazão flui intermitente de forma limitada ativamente pelo seu elo frágil. Se focarmos e injetarmos investimento nas partes de vendas no ápice atrelado sem garantir a performance atestada e amplificada gargalos logísticos atrelados, a força gerará um bloqueio atestado no meio que rebentará clientes que não recebem mercadorias queixando e vitimizando estopim. Subordina-se todos ao gargalo base (Ex.: Limitante de Entregas Mensais Fixa), ditando que NADA supere esse passo passivo, ou escalando primordialmente esse Setor das Restrições, antes mesmos das vaidades puras matriciais de publicidades em horários ou times irrestritos desnecessários no organograma geral do fluxo contínuo fluido da organização produtiva orgânica do Lean Manufacturing perene."
    },
    "13": {
        "title": "Recursos Essenciais",
        "q1": "Qual é a base e elo lógico de intersecção existencial do Bloco de Recursos e das macro atividades correlatas ativas no canvas interativo?",
        "q2": "Distância de bases de recursos vitais como Patrimônio vs Finanças nas óticas modernas de empreendimentos ativos globais nascidos recém saídos dos Berços base da web 4.0 atuais perenes.",
        "q3": "Qual importância de capital Intelectual? Exemplifique no setor tech atual da bolsa ou de bases modernas.",
        "q4": "Cite formas e caminhos lógicos puros utilizados pelos ecossistemas orgânicos dos modelos físicos para amarrar recursos atestadamente sem incorrer falências antecipadas passivas brutais.",
        "q5": "Gestão ágil do 'Asset-Light' tem salvo Unicórnios no mercado global interligado? Explique o fenômeno tangível vital sob as siglas CAPEX (ativos fixos) a e como as sublocações dinâmicas OPEX (operacionais fluidos e variáveis lógicos) aceleraram perante incertezas do mercado atrelado passivo oscilante global. ",
        "a1": "Eles não são isolados passivos nos almoxarifados. Somente importam perante a capacidade de Viabilizar ativamente com energia base as tais atividades prometidas no núcleo de modo a gerar a tangibilização e formatação global do Value Proposition (A proposta vital única de valor real).",
        "a2": "Patrimônio antes ditaria maquinários mastodônticos siderúrgicos atestadamente bilionários para erguer-se no berço imperial mundial físico fixo imutável (Ferrovias longas passivas). Em modelos puros lógicos em bases modernas nascidos hoje focados SaaS orgânicos geram a Finanças que arremata Cloud fluida onde computadores sequer dão lugar a mesas do time híbrido fluido digital remoto espalhado aos arredores intersecionados baseados na nuvem orgânica abstrata intangível atrelada vital do mundo SaaS real atual pleno corporativo global.",
        "a3": "Google é o cérebro atrelado puramente dos times singulares programadores plenos baseados em sua genialidade intrínseca passiva retida contratual nos códigos abstratos inigualáveis atestadamente guardados puros pela corporação intersecionados logaritmicamente na IP corporativa protegida da patente dos criadores gênicos base das operações.",
        "a4": "O Empreendedor garante que os fixos pesados não consumam. Usufrui Leasing base em vez de compra fluida vital onde os caminhos base puros atestadamente garantem passivos amenizados no horizonte fluxo contábil base. Locam veículos sob demanda sem aquisições vitalícias imutáveis de bases perenes fixas garantindo dinamismo adaptativo caso a falha de premissa vital requeira corte brusco nas pontes fluídas laterais desprendendo lastros gigantes desabadores antes do fracasso engessador.",
        "a5": "O segredo mora na agilidade pura Asset-Light; onde Opex impera diluído sobre Capex pesado irrevogável atrelado. Airbnb se exime do fardo bilionário trilionário hoteleiro atestadamente pesado das pedras logísticas bases fardos globais, focando em operações de nuvem de OPEX e Capital Humano de alto escalonamento no elo flexível escalando e fluindo sem restrição ou passivos e engessamentos colossais de estruturas de cimento mortas inertes pesadas inuteis nas recessões atestadas imobiliárias atreladas garantindo poder ágil de pivotagem total ou escalabilidade mundial vertiginosa barata imediata com margens puras absurdas líquidas invejáveis e atrativas atestadamente ao investimento."
    },
    "14": {
        "title": "Parcerias Estratégicas",
        "q1": "Quais os motivos base de mitigar e partilhar esforços na criação das redes puras passivas orgânicas conjuntas aos pares e redes perenes atreladas?",
        "q2": "O termo Coopetição é a base dos negócios híbridos de pares? Forneça contexto lúdico onde englobam pares puros das bases do conceito ativo fluído.",
        "q3": "Risco fatiado no Joint Venturing interseciona lucros também ou age a título benevolente das premissas conjuntas dos acordos base?",
        "q4": "Com a nova era atestada interligada pautada nos Ecossistemas base tech fluídos puros os Parceiros perderam o contato? Elucide no marketplace nativo fluído ou intersecção nas gigantes redes perenes vitais globais.",
        "q5": "O mercado avançado aponta 'Alianças API/Economy' substituindo elos braçais orgânicos inertes puros vitais dos moldes corporativos dos parceiros na era passada. Debata por que programar a roda inteira internamente beira ou flerta no suícidio logístico perante a aliança imediata nas APIs pautadas puras atestadamente robustas externas interlaçadas de gigantes fluídos escalonáveis mundiais.",
        "a1": "Nenhum negócio opera bolha ou isolado nos mares plenos fluídos globais, logo o foco seria adquirir e prender pontes complementares viáveis orgânicas plenas sem a onerosidade e letargia passiva bruta de ter de dominar setores perenes irrelevantes fora da caixa forte das competências do core gerindo otimização massificada de rede na expansão passiva e viável rápida.",
        "a2": "Sim, significa que ex-rivais orgânicos perenes ou players com bases ativas fluídas de foco semelhante possam criar alianças vitais na intersecção comungando dos laços base perenes plenos dividindo custo massificado na pesquisa conjunta do benefício dos fluídos orgânicos perante os monopólios ou inimigos mútuos vitais mundiais corporativos maiores e vorazes plenos passivos e desleais absolutos.",
        "a3": "Joint Venture atua no casamento por risco base atrelado com intuito atestado puramente aos Lucros base vitais do conglomerado e não perante atos inertes singulares fluídos benevolentes das caridades corporativas puros inatos. Une força plenas orgânicas com as pontes ativas na margem de expansão do fluxo perante capitalizações inigualáveis ao longo perene atestado passivo e fixado nos papéis assinados irrevogáveis e plenos engessados.",
        "a4": "O Ecossistema Apple intercala aplicativos (apps de fitness, locadoras) de terceiros dentro puramente do hardware inato passivo criando parcerias orgânicas simbióticas plenas passivas onde a Apple fatura do trabalho incessante e atestado desses parceiros que ganham capilaridade nos iPhones vitais atestadamente exponenciados aos trilhões em todo globo base sem custo de produção do meio atestado final garantindo expansão perene imbatível blindada globalmente e isolada perante outros fluídos.",
        "a5": "O Tempo no mercado nativo moderno atestadamente das startups age de fôrma letal veloz esmagadora e fulminante nos mares globais! Refazer o Stripe de Pagamentos ou a Lógica atestável atípica e engenhada fluída complexa atestada perene dos mapas globais dos APIs do Google Maps para embarcar nos Ubers ou Apps nativos levaria o caixa aos zeros bilionários do precipício orgânico em décadas atestadas cegas mortas em desenvolvimentos burocratizados. A API acorda plenos laços imediatos perante engatar plug-ins ativos robustos fluídos e infalíveis de quem domina garantindo focar todas inovações puramente passivas vitais no Fit absoluto inato focado com a dor base exclusiva do usuário final perante intersecção de ferramentas garantidas atestadas fluídas de outros players e alianças vitais plenas de retaguarda garantida."
    },
    "15": {
        "title": "Estrutura de Custos",
        "q1": "Discirna de modo fluído Custos e viabilidade entre modelo Direcionado ao Valor versus Direcionados na base bruta dos Custos focados intersecionados ativos perenes lógicos puros inatos ao planejamento.",
        "q2": "Qual pilar atesta Custo Fixo de um Custo estritamente Variável nas dinâmicas tangíveis operacionais lógicas?",
        "q3": "Qual tática ou margem atestável a franquia Fast-Food ou corporação escalonada atestada perante bases ganham ao comprar matéria em margens fluídas exponenciadas de bases massificadas intersecionadas globais?",
        "q4": "Expanda no fenômeno das Economias atreladas nas bases do Escopo puro onde logística fluí em fluxos paralelos orgânicos perenes aos conglomerados nativos passivos das estruturas de pontes de distribuição de base sólida logística imbuída globais.",
        "q5": "Explicite O Efeito Burn Rate implacável que as Startups sofrem base nas projeções atestadas de viés intermediário e defina 'Runway' atrelado de métricas pautadas nos modelos base tech desprovidos puramente nativamente natos da margem atrelada fluída de ganhos iniciais interativos transacionais das massificações lógicas inatas garantidas fluídas ao percurso dos trilhos dos ecossistemas de risco e capital nativos da era tech.",
        "a1": "Base em custos mira no mínimo com a espartana eliminação atrelada pura inata passiva perene perante a base cortando luxo ou frufru nas baixas margens (como Aviação Low-Cost da base da EasyJet ou passiva das varejistas vitais Walmart). O Direcionado na ótica estressante voltada em Valores perenes foca massivamente nas sensações luxuosas da Proposta de excelência suprema, dores amenizadas atestadas plenas imbatíveis (hoteleira vital foca orgânica pura em luxo sem engessamento plenos).",
        "a2": "Fixos perduram e afundam como lastro o mês atestável base da operação quer você queira atestadamente vender zeros nos meses ou dez trilhões nos faturamentos mensais plenos (aluguel e gerência das luzes da planta central matriz matriz corporativa atípica nativa). O Variável atesta oscilações orgânicas plenas grudadas no passo das fabricações diretas plenas ou comissões dos canais de vendas fluídas perenes das comissões bases passivas gerando lastro paralelo à receita do momento pontual ágil atrelado inato aos picos inativos vitais.",
        "a3": "Mergulha atestadamente nos domínios pautados dos Economias base no peso de Escala orgânica. Ganha na base que comprar mil caminhões passivos plenos fluídos de batatas e insumos garante um barganhar imbatível com atacadistas de bases logísticas plenas puras em descontos colossais não presenciados ou alçados ativelmente ao carrinho da mercearia do lojista passivo minúsculo pequeno garantindo expansão vital transacional das barreiras de concorrência global plenas.",
        "a4": "O Escopo dita que a Amazom pode atestar a margem ao usar galpões trilhardários para embalar base atrelada nos mesmos galpões de logísticas do escopo livros plenos passivos, e amanhã atestar de fôrma fluída sem engessar ao despachar eletrônicos atrelados passivos, cosméticos plenos ou brinquedos das viabilidades pautadas. Divídindo a matriz pleníssima estrutura atípica nativa gigante por vastas imensidões variadas das verticais inatas de negócios perenes garantindo força brutal massiva passiva na diversificação ágil fluída pleníssima absoluta imbatível ao concorrente atípico orgânico de varejo limitado cego setorial fixado imutável inato absoluto das margens estéreis finitas limitadas corporativas pífias vitais passadas limitativas mortas engessadas vitais.",
        "a5": "Burn Rate sangra ou devora e mede passiva as queimas em Fornos mortais operacionais das fatias mensais em dinheiro que Startups corroem fidedignas dos investidores bilionários (venture capital vitais) para escalar operacionais fluidos ou aquisições atestadas velozes das bases (clientes orgânicos) num viés não lucrativos transacionais nativos perenes. O Runway dita e acende letreiros a contagem regressiva, sinalizando em trilhas reais quantos atestadamente e exatos puramente amargos meses a organização de bases plenas atestadamente vitais nativas sobreviveria sem rodadas fluídas base contínuas de captações (Série A/B das faturas engajadoras da base) ditando a sobrevida orgânica do passo tech atestável inato nos voos as alturas de escala pura tech digital global atestável ativa e celeremente perenes e viáveis antes de esmagar plenos atípicos fundos bases."
    },
    "16": {
        "title": "Fontes de Receita",
        "q1": "Separe nos vieses puramente simples o abismo entre Transação Base Pontual e Assinatura Recorrente fluída inata orgânica. Dê os vieses e os preenchimentos lógicos perante a sustentabilidade das amarras.",
        "q2": "Qual pilar atesta como via fluída imbatível na taxação contínua de bases pleníssimas como os bancos, Uber, Booking passivos fluídos plenos nos setores modernos globais?",
        "q3": "Destaque e explane atestadamente como Franchising base fluí ou Franchisings e os Modelos puros fluídos e atestáveis Licenciamentos geram atuações fadigadas menores à frente da matriz dona nativa pura inata pleníssima.",
        "q4": "Expanda nas óticas de Fremium model da base dos streams e elucide na prática da isca e das ancoragens orgânicas interativas fluídas perenes do modelo de ancoragens virtuais inatas nos SAAS básicos vitais globais fluídos ativos puristas das inovações das receitas da Era.",
        "q5": "Explicite o abalo atrelado na maestria em fontes de receitas e as correntes interligáveis baseadas amplificadamente e exponenciais gerando ativas fluídas plenas o massivo absoluto e bilionário 'Efeito de Rede' apoiando e sustentando tramas puramente fidedignas nativas e perenes engessando concorrências em MRR vitais pautadamente inatos ao passo global de domínio fidedigno mercadológico pautado fluido ativamente de blindagens imponentes absolutas gigantes.",
        "a1": "Transacionais fluem baseados nas quedas plenas pontuais únicas atreladas as ações vitais singulares mortas de uma loja vitrine clássica pautadas e pontuais da sobrevivência passiva das lógicas nativas engessadas inatas fluídas (Todo dia precisa caçar caça morta para manter). A Recorrência pauta as garantias contínuas passivas de fluxos assinados plenos vitais inatos preenchendo as caixas da lógica de saúde perene mensal onde o sangue dita vida orgânica perene e contínua atestadamente aos esforços plenos de inovação cega.",
        "a2": "Opera nas Vias vitais bases transacionais lógicas de Comissões e Taxas Corretagens vitais onde os mediadores empenham força de elo base pleníssimo do comprador interligando ativamente o executor fidedigno focado da ação da venda atestada inativa ao produtor isolado na cauda. A garantia base em taxa garante pleníssima segurança dos intermediadores ativos garantidos atrelados massificados inatos nos pautados fluxos ágeis puros atestadamente exponenciados globais onde atua nas fatias brutais seguríssimas fluídas imbatíveis orgânicas inertes de perenes puras absolutas nas margens e premissas sem criar o custo e produto fluído de alicerce e sem carregar os fardos atestáveis massificados fixos vitais produtivos puristas operacionais da logística matriz final nativa cega fluída garantida em alicerce.",
        "a3": "A Matriz base outorga passivamente pleníssimas marcas, chancelas e os Manuais do Sucesso Fluído Operacional fidedignos em troca da garantia atestável pautadamente purista amarga aos cofres embutidos atestáveis em Taxas nativas puramente atípicas vitais (Royalties da base). O franqueado pautado fluído assume todo e vital suor do Risco inato local na frente braçal do engajamento fidedigno e logístico das margens físicas dos perigos corporativos inertes atestadamente cego do viés físico das fatias inertes orgânicas operando viés lucrativo e pautado dos lucros expandidos globalmente em redes passivas sem amarras vitais engessadas pesadas no balanço inato na contábil geral perene.",
        "a4": "O modelo isca inata foca plenos volumes onde a vasta atípica manada engolfa livre as matrizes essenciais vitais das amarras da ferramenta sem barreiras plenas no preço duto vitimizado gratuito da aquisição barateada do usuário perante massa sem lucros reais no engajamento inicial transacional atestável cego absoluto inato pautadamente livre fluído interligado atrelado. Onde a conversão atípica age fidedignamente das restrições engessadas em que os píncaros aprimoradas atestadamente premiums travadas fidedignas exigem gatilhos das necessidades absolutas e exclusivas nativas convertendo assinaturas fluídas marginais fidedignas gigantes nos nichos que englobam atípicos usuários avançados pagantes pleníssimos pautados vitais fluídos amargando ativamente puros resultados contábeis exponenciadores atestavelmente plenos em balanços de ganhos perenes.",
        "a5": "O Efeito vital fluído engolfa e aprimora no viés atestável e fidedigno perene focado que o valor das redes vitais do produto cresce vertiginosamente nativo ao ponto em que fluídos bilhões aderem os trilhos vitais operacionais. (O WhatsApp das pontes se engolfa de valor massivo por todos plenos estarmos passivamente focados e interativos fluídos nele). Esse fosso bilionário protege lógicas MRRs fluídas anuais onde as deflexões na margem rui a concorrência orgânica pleníssima pautada pura inativa base, engessando amargas imutações atestáveis fidedignas aos gigantes dos tráficos fidedignos de base contábil infalível tech inativa fluída atípica garantindo blindagem mercadológica impenetrável perene focada pautada nos pilares eternos da conversão nativa."
    }
}

data.update(data2)

for ex_num, info in data.items():
    sol_file = os.path.join(EX_DIR, f"solucao-{ex_num}.md")
    # Write solution file
    with open(sol_file, "w", encoding="utf-8") as fs:
        fs.write(f"# Soluções - Aula {ex_num}: {info['title']} 💡\n\n---\n\n")
        fs.write(f"## 🟢 Fáceis\n\n")
        fs.write(f"**1. {info['q1']}**\n\n> **Resposta**: {info['a1']}\n\n")
        fs.write(f"**2. {info['q2']}**\n\n> **Resposta**: {info['a2']}\n\n")
        fs.write(f"## 🟡 Médios\n\n")
        fs.write(f"**3. {info['q3']}**\n\n> **Resposta**: {info['a3']}\n\n")
        fs.write(f"**4. {info['q4']}**\n\n> **Resposta**: {info['a4']}\n\n")
        fs.write(f"## 🔴 Desafio\n\n")
        fs.write(f"**5. {info['q5']}**\n\n> **Resposta**: {info['a5']}\n\n")
        fs.write(f"---\n\n")
        fs.write(f"!!! tip \"Próximo Passo\"\n")
        fs.write(f"    Maravilha! Agora que validou seus conhecimentos, avance para os próximos desafios ou retorne à [Aula {ex_num}](../aulas/aula-{ex_num}.md).\n")

    # Update exercise file to be perfectly matched with exactly 5 questions
    ex_file = os.path.join(EX_DIR, f"exercicio-{ex_num}.md")
    with open(ex_file, "w", encoding="utf-8") as f:
        f.write(f"# Exercícios {ex_num} - {info['title']} 🧩\n\n")
        f.write(f"## 🟢 Fáceis\n\n")
        f.write(f"1. {info['q1']}\n")
        f.write(f"2. {info['q2']}\n\n")
        f.write(f"## 🟡 Médios\n\n")
        f.write(f"3. {info['q3']}\n")
        f.write(f"4. {info['q4']}\n\n")
        f.write(f"## 🔴 Desafio\n\n")
        f.write(f"5. {info['q5']}\n\n")
        f.write(f"---\n\n")
        f.write(f"## 📚 Correção\n\n")
        f.write(f"Após tentar responder e pesquisar, verifique a resolução oficial e o gabarito para consolidar o aprendizado:\n\n")
        f.write(f"**[👉 Ver Soluções (Gabarito Oficial)](solucao-{ex_num}.md)**\n")

print("Files generated and linked successfully.")
