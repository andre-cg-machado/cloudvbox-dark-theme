# cloudvBOX Dark Theme

<div align="center">
  <img src="https://cloudvbox.com/wp-content/uploads/2024/08/logo-preto.png" alt="cloudvBOX Logo" width="200"/>
  
  **cloudvBOX Dark Theme for JupyterLab**
  
  [![PyPI version](https://badge.fury.io/py/cloudvbox-dark-theme.svg)](https://badge.fury.io/py/cloudvbox-dark-theme)
  [![Python Support](https://img.shields.io/pypi/pyversions/cloudvbox-dark-theme.svg)](https://pypi.org/project/cloudvbox-dark-theme/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Downloads](https://pepy.tech/badge/cloudvbox-dark-theme)](https://pepy.tech/project/cloudvbox-dark-theme)
</div>

## 🎨 Visão Geral

O **cloudvBOX Dark Theme** é um tema profissional escuro desenvolvido especificamente para Jupyter Notebook e JupyterLab, incorporando a identidade visual moderna do cloudvBOX. Este tema oferece uma experiência visual elegante e profissional para cientistas de dados, desenvolvedores e pesquisadores.

### ✨ Características Principais

- **🌙 Design Escuro Profissional**: Fundo escuro (#012837) que reduz o cansaço visual
- **🎯 Cor de Destaque Única**: Ciano vibrante (#55FCFF) da identidade cloudvBOX
- **🖼️ Logo Integrado**: Logo cloudvBOX elegantemente posicionado no header
- **📱 Design Responsivo**: Funciona perfeitamente em desktop e mobile
- **🔧 Syntax Highlighting Otimizado**: Cores cuidadosamente selecionadas para melhor legibilidade
- **⚡ Instalação Simples**: Instalação com um comando via pip
- **🔄 Compatibilidade Ampla**: Suporte para Jupyter Notebook e JupyterLab

### 🎨 Paleta de Cores

| Elemento | Cor | Hex |
|----------|-----|-----|
| Fundo Principal | Azul Escuro | `#012837` |
| Cor de Destaque | Ciano | `#55FCFF` |
| Texto Principal | Branco | `#ffffff` |
| Texto Secundário | Cinza Claro | `#d1d5db` |
| Botões Primários | Azul | `#3b82f6` |
| Cards/Painéis | Cinza Escuro | `#1f2937` |




## 🚀 Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Jupyter Notebook 6.0+ ou JupyterLab 3.0+

### Instalação via pip

```bash
# Instalar o pacote
pip install cloudvbox-dark-theme

# Aplicar o tema
cloudvbox-theme-install
```

### Instalação via poetry

```bash
# Adicionar ao projeto
poetry add cloudvbox-dark-theme

# Aplicar o tema
poetry run cloudvbox-theme-install
```

### Instalação para Desenvolvimento

```bash
# Clonar o repositório
git clone https://github.com/cloudvbox/cloudvbox-dark-theme.git
cd cloudvbox-dark-theme

# Instalar em modo desenvolvimento
pip install -e .

# Aplicar o tema
cloudvbox-theme-install
```

## 🎯 Uso Rápido

Após a instalação, reinicie o Jupyter Notebook ou JupyterLab para aplicar o tema:

```bash
# Para Jupyter Notebook
jupyter notebook

# Para JupyterLab
jupyter lab
```

O tema será aplicado automaticamente em todas as sessões futuras.

## 📋 Comandos Disponíveis

O pacote inclui vários comandos de linha de comando para gerenciar o tema:

### Instalação e Remoção

```bash
# Instalar o tema
cloudvbox-theme-install

# Remover o tema
cloudvbox-theme-uninstall

# Interface completa (recomendado)
cloudvbox-theme install
cloudvbox-theme uninstall
```

### Informações e Ajuda

```bash
# Mostrar informações do tema
cloudvbox-theme --info

# Mostrar versão
cloudvbox-theme --version

# Ajuda completa
cloudvbox-theme --help
```

### Opções Avançadas

```bash
# Instalação forçada (sem confirmação)
cloudvbox-theme install --force

# Modo verboso (mais detalhes)
cloudvbox-theme install --verbose

# Combinação de opções
cloudvbox-theme install --force --verbose
```


## 🖼️ Screenshots

### Jupyter Notebook
![Jupyter Notebook com cloudvBOX Dark Theme](docs/images/notebook-screenshot.png)

### JupyterLab
![JupyterLab com cloudvBOX Dark Theme](docs/images/jupyterlab-screenshot.png)

### Células de Código
![Células de código com syntax highlighting](docs/images/code-cells-screenshot.png)

### Células de Markdown
![Células de markdown renderizadas](docs/images/markdown-cells-screenshot.png)

## 🔧 Personalização

### Modificando Cores

Você pode personalizar as cores do tema editando o arquivo CSS:

```css
:root {
    /* Personalizar cor principal */
    --cloudvbox-primary: #55FCFF;
    
    /* Personalizar fundo */
    --cloudvbox-dark-bg: #012837;
    
    /* Personalizar texto */
    --cloudvbox-text-primary: #ffffff;
}
```

### Adicionando Estilos Customizados

Crie um arquivo `custom-extra.css` no diretório custom do Jupyter:

```bash
# Localizar diretório custom
jupyter --config-dir
```

```css
/* Exemplo de customização adicional */
.cell.selected {
    border-color: #ff6b6b !important;
}

.CodeMirror {
    font-size: 16px !important;
}
```

### Configuração Avançada

Para configurações mais avançadas, você pode usar a API Python:

```python
from cloudvbox_dark_theme import theme_config

# Acessar configurações
config = theme_config
print(config.colors)

# Gerar variáveis CSS customizadas
css_vars = config.get_css_variables()
print(css_vars)
```

## 🔍 Troubleshooting

### Tema não aparece após instalação

1. **Verificar instalação**:
   ```bash
   cloudvbox-theme --info
   ```

2. **Reinstalar o tema**:
   ```bash
   cloudvbox-theme-uninstall
   cloudvbox-theme-install
   ```

3. **Limpar cache do navegador**:
   - Pressione `Ctrl+F5` (Windows/Linux) ou `Cmd+Shift+R` (Mac)

### Logo não aparece

1. **Verificar arquivos de imagem**:
   ```bash
   # Verificar se o logo foi copiado
   ls ~/.jupyter/custom/images/
   ```

2. **Verificar permissões**:
   ```bash
   chmod 644 ~/.jupyter/images/logo-branco.png
   ```

### Conflitos com outros temas

1. **Remover outros temas**:
   ```bash
   # Backup do custom.css atual
   cp ~/.jupyter/custom/custom.css ~/.jupyter/custom/custom.css.backup
   
   # Reinstalar tema cloudvBOX
   cloudvbox-theme-install
   ```

### Problemas de compatibilidade

1. **Verificar versões**:
   ```bash
   jupyter --version
   jupyter lab --version
   ```

2. **Atualizar Jupyter**:
   ```bash
   pip install --upgrade jupyter jupyterlab
   ```


## 🤝 Contribuindo

Contribuições são bem-vindas! Veja como você pode ajudar:

### Reportando Bugs

1. Verifique se o bug já foi reportado nas [Issues](https://github.com/cloudvbox/cloudvbox-dark-theme/issues)
2. Crie uma nova issue com:
   - Descrição detalhada do problema
   - Passos para reproduzir
   - Screenshots (se aplicável)
   - Informações do sistema (`cloudvbox-theme --info`)

### Sugerindo Melhorias

1. Abra uma issue com a tag `enhancement`
2. Descreva a melhoria proposta
3. Explique por que seria útil
4. Forneça exemplos ou mockups se possível

### Desenvolvendo

1. **Fork o repositório**
2. **Clone seu fork**:
   ```bash
   git clone https://github.com/seu-usuario/cloudvbox-dark-theme.git
   cd cloudvbox-dark-theme
   ```

3. **Criar branch para feature**:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

4. **Instalar dependências de desenvolvimento**:
   ```bash
   pip install -e ".[dev]"
   ```

5. **Fazer suas alterações**
6. **Testar as alterações**:
   ```bash
   # Instalar tema local
   cloudvbox-theme-install
   
   # Testar no Jupyter
   jupyter notebook
   jupyter lab
   ```

7. **Commit e push**:
   ```bash
   git add .
   git commit -m "feat: adicionar nova funcionalidade"
   git push origin feature/nova-funcionalidade
   ```

8. **Criar Pull Request**

### Padrões de Código

- Use **Black** para formatação Python
- Siga **PEP 8** para estilo Python
- Use **Prettier** para formatação CSS/JS
- Adicione comentários explicativos
- Mantenha compatibilidade com versões suportadas

### Testando

```bash
# Executar testes
pytest

# Verificar cobertura
pytest --cov=cloudvbox_dark_theme

# Linting
flake8 cloudvbox_dark_theme/
black --check cloudvbox_dark_theme/
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2025 cloudvBOX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Agradecimentos

- **Equipe cloudvBOX** - Pela identidade visual e inspiração
- **Projeto Jupyter** - Pela plataforma incrível
- **Comunidade Open Source** - Pelas ferramentas e bibliotecas utilizadas

## 📞 Suporte

- **Website**: [cloudvbox.com](https://cloudvbox.com)
- **Email**: contato@cloudvbox.com
- **GitHub Issues**: [Reportar problema](https://github.com/cloudvbox/cloudvbox-dark-theme/issues)
- **Documentação**: [GitHub Wiki](https://github.com/cloudvbox/cloudvbox-dark-theme/wiki)

## 🔗 Links Úteis

- [Jupyter Notebook](https://jupyter.org/)
- [JupyterLab](https://jupyterlab.readthedocs.io/)
- [cloudvBOX](https://cloudvbox.com)
- [Guia de Contribuição](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

---

<div align="center">
  <p>Feito com ❤️ pela equipe <strong>cloudvBOX</strong></p>
  <p>
    <a href="https://cloudvbox.com">Website</a> •
    <a href="https://github.com/cloudvbox">GitHub</a> •
    <a href="mailto:contato@cloudvbox.com">Contato</a>
  </p>
</div>

