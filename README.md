<div align="center">
  <h1>Agent API Cookiecutter</h1>
  <h3>Building Agent Projects without losing your mind</h3>
</div>

</br>

<p align="center">
    <img src="static/logo.png" alt="General Diagram" width="600">
</p>

## Table of Contents

- [Getting Started](#projects)
- [Contributors](#contributors)
- [License](#license)

## The motivation behind this cookiecutter

Ever since I started creating content, one question keeps coming up:

> How should I structure my Agent projects? 🤔

This cookiecutter is my best attempt to answer that question! It contains the structure I follow when creating Agent APIs.

So, give it a try and let me know what you think!

```
example-agent-api
├── Dockerfile
├── Makefile
├── README.md
├── data
├── docker-compose.yaml
├── notebooks
├── pyproject.toml
├── src
│   └── example_agent_api
│       ├── __init__.py
│       ├── application
│       │   ├── __init__.py
│       │   ├── chat_service
│       │   ├── evaluation_service
│       │   ├── ingest_documents_service
│       │   └── reset_memory_service
│       ├── config.py
│       ├── domain
│       │   ├── __init__.py
│       │   ├── exceptions.py
│       │   ├── memory
│       │   ├── prompts
│       │   ├── tools
│       │   └── utils.py
│       └── infrastructure
│           ├── __init__.py
│           ├── api
│           │   ├── __init__.py
│           │   ├── main.py
│           │   └── models.py
│           ├── db
│           ├── llm_providers
│           ├── mcp_clients
│           └── monitoring
├── static
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_example_agent_api.py
```

---

<table style="border-collapse: collapse; border: none;">
  <tr style="border: none;">
    <td width="20%" style="border: none;">
      <a href="https://theneuralmaze.substack.com/" aria-label="The Neural Maze">
        <img src="https://avatars.githubusercontent.com/u/151655127?s=400&u=2fff53e8c195ac155e5c8ee65c6ba683a72e655f&v=4" alt="The Neural Maze Logo" width="150"/>
      </a>
    </td>
    <td width="80%" style="border: none;">
      <div>
        <h2>📬 Stay Updated</h2>
        <p><b><a href="https://theneuralmaze.substack.com/">Join The Neural Maze</a></b> and learn to build AI Systems that actually work, from principles to production. Every Wednesday, directly to your inbox. Don't miss out!</p>
      </div>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://theneuralmaze.substack.com/">
    <img src="https://img.shields.io/static/v1?label&logo=substack&message=Subscribe%20Now&style=for-the-badge&color=black&scale=2" alt="Subscribe Now" height="40">
  </a>
</p>

## Getting Started




## Contributors

<table>
  <tr>
    <td align="center"><img src="https://github.com/MichaelisTrofficus.png" width="100" style="border-radius:50%;"/></td>
    <td>
      <strong>Miguel Otero Pedrido | Senior ML / AI Engineer </strong><br />
      <i>Founder of The Neural Maze. Rick and Morty fan.</i><br /><br />
      <a href="https://www.linkedin.com/in/migueloteropedrido/">LinkedIn</a><br />
      <a href="https://www.youtube.com/@TheNeuralMaze">YouTube</a><br />
      <a href="https://theneuralmaze.substack.com/">The Neural Maze Newsletter</a>
    </td>
  </tr>
</table>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
