# MCP Client

A Python client for interacting with MCP (Machine Control Platform) API using FastAPI and Streamlit.

## ⚠️ Work in Progress

This project is currently under active development. Features and APIs may change without notice. We welcome contributions and feedback from the community.

## Features

- FastAPI-based API client for MCP services
- Streamlit-based frontend interface
- Anthropic integration for AI capabilities
- Environment-based configuration management
- Rich console output for better debugging

## Installation

1. Clone the repository:
```bash
git clone https://github.com/seonokkim/mcp-client.git
cd mcp-client
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Usage

1. Set up your environment variables:
```bash
cp .env.example .env  # Copy example environment file
# Edit .env with your API keys and configurations
```

2. Run the Streamlit frontend:
```bash
streamlit run front/main.py
```

3. Run the FastAPI backend:
```bash
uvicorn api.main:app --reload
```

## Project Structure

```
mcp-client/
├── api/         # FastAPI backend implementation
├── front/       # Streamlit frontend implementation
├── .env.example # Example environment configuration
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project is based on the work of [Alejandro's MCP client implementation](https://github.com/alejandro-ao/mcp-client-python-example), which served as a foundation for this project.

## Contact

Seonok Kim - seonokrkim@email.com

Project Link: [https://github.com/seonokkim/mcp-client](https://github.com/seonokkim/mcp-client)