"""Ragfood: Making knowledge from documents accessible for chats with LLMs.

Ragfood is a comprehensive document processing and knowledge extraction system
that integrates with Calibre e-book management to provide LLM-powered document
querying capabilities.

Key Components:
- Selectable: Customizable selection widgets with radio/multi/radiox behavior
- Mediator: Communication coordination between application components
- States: Global state constants for error handling and status reporting
- Calibre: Integration with Calibre e-book library management
- Booklist: Selectable list interface for document browsing
- PDFView: PDF preview with thumbnail generation and metadata display
- Ragfood: Main application class coordinating the complete workflow

Features:
- Document library management via Calibre integration
- PDF preview with thumbnail navigation
- Automatic sample library creation for testing
- Mediator pattern for loose component coupling
- Comprehensive error handling and status reporting
- Jupyter widget-based interactive interface

Dependencies:
- Calibre: E-book management software
- ipywidgets: Interactive Jupyter widgets
- PyPDF2: PDF processing and metadata extraction
- pdf2image: PDF thumbnail generation
- poppler-utils: System dependency for pdf2image

Example:
    >>> from Ragfood.ragfood import Ragfood
    >>> app = Ragfood()
    >>> display(app.widget)
"""

__version__ = "0.0.1"
