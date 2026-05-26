from agent import build_search_agent ,build_search_reader_agent ,writter_chain,critic_chain


def run_research_pipeline(topic: str):

    state = {}

    # Search process 
    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"Find recent and reliable information about {topic}"
            )
        ]
    })

    search_text = search_result["messages"][-1].content
    state["search_result"] = search_text

    # Read URLs
    reader_agent = build_search_reader_agent()

    scraped_content = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"Read and summarize these URLs:\n{search_text}"
            )
        ]
    })

    scraped_text = scraped_content["messages"][-1].content
    state["research_data"] = scraped_text

    # Write report
    report = writter_chain.invoke({
        "query": topic,
        "research_data": scraped_text
    })

    state["report"] = report

    # Critic review
    review = critic_chain.invoke({
        "query": topic,
        "report": report
    })

    state["review"] = review

    return state


if __name__ == "__main__":

    topic = input("\nEnter research topic: ")

    result = run_research_pipeline(topic)

    print("\n===== REPORT =====\n")
    print(result["report"])

    print("\n===== REVIEW =====\n")
    print(result["review"])