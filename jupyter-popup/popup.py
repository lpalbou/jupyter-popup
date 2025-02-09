from IPython.display import HTML
import json

def create_popup(message, title="Notice"):
    """
    Creates a popup dialog in a Jupyter notebook that stays fixed on screen.
    
    Parameters
    ----------
    message : str
        The content to display in the popup. Can include HTML.
    title : str, optional
        The title of the popup window. Defaults to "Notice".
        
    Returns
    -------
    IPython.display.HTML
        The HTML display object that creates the popup.
        
    Examples
    --------
    >>> create_popup("Hello World!", "Greeting")
    >>> 
    >>> # With HTML content
    >>> html_content = "<div><h3>Title</h3><p>Content</p></div>"
    >>> create_popup(html_content, "HTML Example")
    """
    # Properly escape the content for JavaScript
    escaped_message = json.dumps(message)[1:-1]
    escaped_title = json.dumps(title)[1:-1]
    
    html = f"""
    <div id="temp-popup-container">
        <script>
            (() => {{
                try {{
                    const overlay = document.createElement('div');
                    const popup = document.createElement('div');
                    
                    overlay.style.cssText = `
                        position: fixed;
                        top: 0;
                        left: 0;
                        width: 100vw;
                        height: 100vh;
                        background: rgba(0, 0, 0, 0.5);
                        z-index: 2147483646;
                    `;
                    
                    popup.style.cssText = `
                        position: fixed;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        background: white;
                        padding: 0;
                        border-radius: 8px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                        width: min(600px, 90vw);
                        max-height: 90vh;
                        display: flex;
                        flex-direction: column;
                        z-index: 2147483647;
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                        color: black;
                    `;
                    
                    const header = document.createElement('div');
                    header.style.cssText = `
                        padding: 16px;
                        border-bottom: 1px solid #eee;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        background: white;
                        border-radius: 8px 8px 0 0;
                    `;
                    
                    const titleDiv = document.createElement('div');
                    titleDiv.style.cssText = `
                        font-weight: bold;
                        font-size: 16px;
                        color: black;
                    `;
                    titleDiv.textContent = "{escaped_title}";
                    header.appendChild(titleDiv);
                    
                    const closeBtn = document.createElement('button');
                    closeBtn.style.cssText = `
                        cursor: pointer;
                        font-size: 24px;
                        border: none;
                        background: none;
                        color: #666;
                        padding: 4px 8px;
                    `;
                    closeBtn.textContent = '×';
                    header.appendChild(closeBtn);
                    
                    const content = document.createElement('div');
                    content.style.cssText = `
                        padding: 16px;
                        overflow-y: auto;
                        max-height: calc(90vh - 70px);
                        color: black;
                    `;
                    content.innerHTML = "{escaped_message}";
                    
                    popup.appendChild(header);
                    popup.appendChild(content);
                    
                    const closePopup = () => {{
                        overlay.remove();
                        popup.remove();
                    }};
                    
                    closeBtn.onclick = closePopup;
                    overlay.onclick = closePopup;
                    
                    let currentElement = document.currentScript.parentElement;
                    while (currentElement && currentElement.tagName !== 'BODY') {{
                        currentElement = currentElement.parentElement;
                    }}
                    
                    if (currentElement && currentElement.tagName === 'BODY') {{
                        currentElement.appendChild(overlay);
                        currentElement.appendChild(popup);
                    }}
                    
                    const container = document.getElementById('temp-popup-container');
                    if (container) container.remove();
                }} catch (error) {{
                    console.error('Popup creation error:', error);
                }}
            }})();
        </script>
    </div>
    """
    return HTML(html)