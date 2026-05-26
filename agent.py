from langchain.agents import create_agent 
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search ,scrape_url

from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

model = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature=0
)


def build_search_agent():
    return create_agent(
        model= model,
        tools= [web_search]
    )
    
def build_search_reader_agent():
    return create_agent(
        model= model,
        tools= [scrape_url]
    )
    

writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert research report writer.

        Your job is to:
        - Analyze the collected research.
        - Extract key insights.
        - Remove duplicate information.
        - Cite sources whenever possible.
        - Write a professional report.

        Report Structure:

        # Executive Summary

        # Key Findings

        # Detailed Analysis

        # Sources

        # Conclusion
        """
    ),
    (
        "human",
        """
        Research Topic:
        {query}

        Collected Information:
        {research_data}

        Generate a comprehensive report.
        """
    )
])

writter_chain = writer_prompt | model | parser


critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a senior research reviewer and quality assurance expert.

        Your task is to critically evaluate a research report.

        Review the report for:

        1. Accuracy
           - Are there unsupported claims?
           - Are conclusions justified by the evidence?

        2. Completeness
           - Are important aspects of the topic missing?
           - Are there unanswered questions?

        3. Evidence Quality
           - Are sources reliable?
           - Is sufficient evidence provided?

        4. Logical Consistency
           - Are there contradictions?
           - Are arguments coherent and well-supported?

        5. Structure & Clarity
           - Is the report easy to understand?
           - Are sections organized properly?

        6. Source Validation
           - Are sources properly listed?
           - Are citations relevant to the claims made?

        Return your review in the following format:

        ## Overall Score
        Give a score from 1-10

        ## Strengths
        - Point 1
        - Point 2

        ## Weaknesses
        - Point 1
        - Point 2

        ## Missing Information
        - Missing topic 1
        - Missing topic 2

        ## Suggested Improvements
        - Improvement 1
        - Improvement 2

        ## Final Verdict
        PASS or REVISE

        Be objective, critical, and specific.
        """
    ),
    (
        "human",
        """
        Research Topic:
        {query}

        Generated Report:

        {report}

        Perform a detailed critical review.
        """
    )
])

critic_chain = critic_prompt | model | parser



