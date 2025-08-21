# mocktests - CodePori AI Code Generation System

This repository contains **CodePori**, a sophisticated AI-powered code generation system that creates complete, multi-module Python projects using multi-agent AI technology.

## Overview

CodePori is a novel system designed to automate code generation for extensive and complex software projects given high-level descriptions. It employs LLM-based multi-AI agents to handle creative and challenging tasks including:

- System design and architecture
- Code development and implementation  
- Code review and optimization
- Code verification and testing
- Test engineering and validation

## Key Features

- **Multi-Agent Architecture**: Specialized AI agents for different development tasks
- **Complete Project Generation**: Creates full project structures with proper Python packaging
- **Automated Testing**: Generates comprehensive test suites using pytest
- **Modern Python Standards**: Uses pyproject.toml, src/ layout, and modern packaging
- **AI Model Integration**: Communicates with Gemini AI models via proxy server
- **Debugging Loop**: Automatically fixes issues using AI-powered debugging

## Project Structure

```
mocktests/
├── gemini-flask-57-2.py      # Main orchestration script
├── requirements.txt          # Python dependencies  
├── PROJECT_CONFIG.md         # Detailed project configuration
├── test_repository.py        # Repository validation tests
├── CodePori.zip             # Archive with prompt files and examples
└── README.md                # This file
```

## Quick Start

### Prerequisites

- Python 3.10+ (tested with 3.12)
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/perlman-izzy/mocktests.git
cd mocktests
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Smoke Test

Verify the installation:
```bash
python -c "import pathlib, requests, json; print('SMOKE')"
```

### Running Tests

```bash
python -m pytest -q
```

### Basic Usage

The system requires a Gemini API proxy server. For development/testing:

```bash
# Set environment variable for proxy (optional, defaults to localhost:8000)
export GEMINI_PROXY_BASE=http://localhost:8000

# Run the code generation pipeline
python gemini-flask-57-2.py
```

## Dependencies

### Core Dependencies
- **requests**: HTTP client for AI API communication
- **pytest**: Testing framework

### Generated Project Dependencies
Generated projects may include additional dependencies based on requirements:
- Standard library modules (json, pathlib, subprocess, etc.)
- Project-specific packages as determined by AI agents

## Configuration

See `PROJECT_CONFIG.md` for complete configuration details including:
- Language and tool specifications
- Test command configuration
- Environment variable requirements
- External service dependencies
- Performance guardrails

## Generated Output

The system creates complete Python projects in `output/code/` with:
- Proper `pyproject.toml` configuration
- Source code in `src/` directory structure
- Comprehensive test suites in `tests/`
- Documentation and README files
- Requirements specification

## Testing Strategy

The repository includes multiple testing approaches:

1. **Repository Tests**: Validate basic functionality and dependencies
2. **Generated Project Tests**: Pytest-based test suites for generated code
3. **Integration Tests**: End-to-end pipeline validation
4. **Smoke Tests**: Quick validation of core imports and functionality

## AI Integration

CodePori integrates with Gemini AI models through a Flask proxy server that handles:
- API key rotation and management
- Rate limiting and retry logic
- Request routing and fallback models
- Health monitoring and status reporting

## Development

### Running Repository Validation

```bash
python test_repository.py
```

### Code Generation Pipeline

The main pipeline consists of:

1. **Planning Phase**: AI agent creates project architecture
2. **Generation Phase**: Multiple AI agents create code modules
3. **Finalization Phase**: AI agent creates documentation and requirements
4. **Debug Loop**: Automated testing and AI-powered bug fixing

## Contributing

1. Follow Python best practices and PEP 8 style guidelines
2. Add tests for new functionality
3. Update documentation as needed
4. Ensure compatibility with Python 3.10+

## License

This project follows the MIT License. See the CodePori documentation for specific licensing terms.

## Contact

For questions or feedback:
- Email: zeeshan.rasheed@tuni.fi
- Follow GPT Lab: https://www.linkedin.com/company/gpt-lab/posts/

## Citation

```bibtex
@article{rasheed2024codepori,
  title={Codepori: Large scale model for autonomous software development by using multi-agents},
  author={Rasheed, Zeeshan and Waseem, Muhammad and Saari, Mika and Syst{\"a}, Kari and Abrahamsson, Pekka},
  journal={arXiv preprint arXiv:2402.01411},
  year={2024},
}
```