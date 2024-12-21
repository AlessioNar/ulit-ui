import streamlit as st
import pandas as pd

def main():
    st.set_page_config(
        page_title="TULIT - The Universal Legal Informatics Toolkit",
        page_icon="👋",
    )

    st.write("# TULIT")
    st.write("## The Universal Legal Informatics Toolkit 👋")

    st.sidebar.success("Test the demo by clicking on the sidebar options.")
    tabs = st.tabs(["Home", "About", "Contribute", "Contact"])

    with tabs[0]:
        st.markdown(
            """
            The Universal Legal Informatics Toolkit is an open-source web app that aims to
            overcome technical interoperability barriers of legal data to enable additional use cases.
            
            It provides functionalities to:
            - Download a document from Cellar
            - Parse legal documents in various standard formats (Akoma Ntoso, FORMEX4, and XHTML)
            
            **👈 Select a demo from the sidebar** to see some examples
            of what ULIT can do!
            
            ### Want to learn more?
            Explore the tabs above to find out more about the project, how to contribute, and how to get in touch with us.
            """
        )

    with tabs[1]:
        st.markdown(
            """
            ## About
            
            TULIT is a web application which aims to overcome technical interoperability barriers when accessing and processing legal data. Its mission is to provide a comprehensive toolkit that supports:
            - the retrieval of legislative resources of a variety of EU entities
            - the transformation of such legal data into a python-friendly format to enable further use cases.
            
            As of now, TULIT supports the download of data from the following data sources:
            - [Cellar](https://op.europa.eu/en/web/cellar#:~:text=Cellar%20is%20the%20common%20data%20repository%20of%20the,order%20to%20be%20used%20by%20humans%20and%20machines.), the Semantic Repository of the Publications Office of the EU
            - [Normattiva](https://www.normattiva.it/), the Italian official legal database
            
            Additionally, TULIT provides parsing capabilities for legal documents in the following formats:
            - Akoma Ntoso
            - FORMEX4
            - XHTML
            
            ### Vision
            Our vision is to create a universal platform that simplifies the handling of legal data, making it accessible and usable for everyone.
            """
        )

    with tabs[2]:
        st.markdown(
            """
            ## Contribute
            
            We welcome contributions from the community! Whether you're a developer, legal expert, or just someone interested in legal informatics, there are many ways you can help:
            
            - **Code Contributions**: Help us improve the toolkit by fixing bugs, adding new features, or enhancing existing ones.
            - **Documentation**: Improve our documentation to make it easier for others to use and contribute to the project.
            - **Testing**: Test the toolkit and report any issues or suggest improvements.
            
            ### How to Contribute
            1. Fork the repository on GitHub.
            2. Create a new branch for your feature or bug fix.
            3. Submit a pull request with a detailed description of your changes.
            
            We appreciate your support and look forward to your contributions!
            """
        )

    with tabs[3]:
        st.markdown(
            """
            ## Contact
            
            If you have any questions, suggestions, or feedback, feel free to reach out to us. We're always happy to hear from our users and contributors.
            
            ### Contact Information
            - **Email**: support@tulit.org
            - **GitHub**: [TULIT Repository](https://github.com/your-repo/tulit)
            - **Twitter**: [@TULIT_Toolkit](https://twitter.com/TULIT_Toolkit)
            
            ### Join Our Community
            Connect with other users and contributors on our [Discord server](https://discord.gg/your-invite-link) to discuss ideas, share knowledge, and collaborate on the project.
            """
        )

if __name__ == "__main__":
    main()