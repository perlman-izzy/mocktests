PROJECT NAME: mocktests - CodePori AI-Powered Code Generation System
REPO: https://github.com/perlman-izzy/mocktests (public)

LANGUAGES/TOOLS (check all that apply):
- [x] Python  (version: 3.12+, but supports 3.10+)
- [ ] Node/PNPM/NPM (node version: N/A)
- [ ] Java/Gradle (jdk: N/A)
- [ ] .NET (sdk: N/A)
- [ ] Android SDK (no)
- [x] Other: AI/LLM integration via HTTP proxy, requests library for API communication

PYTHON PACKAGING (pick one):
- [ ] requirements.txt
- [x] pyproject.toml (backend: setuptools)
- [ ] none (infer packages from imports)

TEST COMMANDS (write exact commands; I'll wire them):
- Unit tests: python -m pytest -q
- Lint (optional): N/A (no linter configured in current codebase)
- Build (optional): N/A (no build step required, pure Python)

ENTRY/SMOKE (short, non-blocking check):
- Python: python -c "import pathlib, requests, json; print('SMOKE')"
- Node: N/A
- Other: python test_repository.py

SYSTEM PACKAGES NEEDED (apt): 
python3-dev, python3-pip (base Python development packages - no special native dependencies)

NATIVE/LIB EXTRAS:
- TA-Lib needed? no
- OpenCV? no  FFMPEG? no
- CUDA/GPU? no   (Jules VMs are CPU-only—confirmed)

EXTERNAL SERVICES NEEDED AT TEST TIME (prefer NONE):
Flask proxy server on localhost:8000 (for Gemini API communication) - can be stubbed/mocked for tests

ENV VARS REQUIRED TO IMPORT/RUN TESTS (safe dummy values ok):
GEMINI_PROXY_BASE=http://localhost:8000 (can use http://mock-server:8000 for CI)

TIME/LONG-RUNNING GUARDRAILS:
- Max setup time: 5 min
- Do NOT start servers, websockets, infinite loops (agree: yes)

SPECIAL NOTES:
- This is a sophisticated AI-powered code generation system that creates multi-module Python projects
- Main entry point is gemini-flask-57-2.py which orchestrates AI agents for: planning, coding, testing, debugging
- Generated projects use modern Python packaging (pyproject.toml with setuptools backend)  
- System generates comprehensive test suites using pytest framework
- Dependencies include: requests (for AI API calls), pytest (testing), various utility libraries
- The system expects specific prompt files (*.txt) for AI agent instructions - these are included in CodePori.zip
- Generated code follows modern Python practices with proper project structure (src/ layout)
- For CI/testing: can mock the Gemini proxy server to avoid external API dependencies
- Core functionality is code generation, so primary tests should focus on the generation pipeline rather than generated output