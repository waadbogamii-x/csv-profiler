import streamlit as st
import csv
import json
from pathlib import Path
report = st.session_state.get("report")

from io import StringIO
from src.csv_profiler.profile import profile_rows
from src.csv_profiler.render import render_markdown

st.set_page_config(page_title="CSV Profiler", layout="wide")

st.title("CSV Profiler")
st.caption("This Streamlit app")

st.sidebar.header("Choose an option")

uploaded = st.file_uploader("Upload a CSV", type=["csv"])
show_preview = st.sidebar.checkbox("Show preview", value=True)
rows = None

if uploaded is not None:
  text = uploaded.getvalue().decode("utf-8-sig")
  rows = list(csv.DictReader(StringIO(text)))
  if len(rows) == 0:
     st.error("CSV has no data. Upload a CSV with at least 1 row.")
     st.stop()
  if len(rows[0]) == 0:
     st.warning("CSV has no headers (no columns detected).")


if show_preview:
    if rows is None:
        st.info("Upload a CSV to see preview.")
    elif len(rows) == 0:
        st.warning("CSV has no data rows.")
    else:
        st.subheader("Preview")
        st.write(rows[:5])


if rows is not None:
 if len(rows) > 0:
     if st.button("Generate report"):
       st.session_state["report"] = profile_rows(rows)

       
       
       n_rows = len(rows)
       n_cols = len(rows[0]) if n_rows > 0 else 0


       cols = st.columns(2)
       cols[0].metric("Rows", n_rows)
       cols[1].metric("Columns", n_cols)


if report is not None:
   st.subheader("Columns")
 
   with st.expander("Markdown preview", expanded=False):
      st.markdown(render_markdown(report))

      #تاسك 5
   report_name = "report"


   json_file = report_name + ".json"
   md_file = report_name + ".md"

   json_text = json.dumps(report, indent=2, ensure_ascii=False)
   md_text = render_markdown(report)

   c1, c2 = st.columns(2)
   c1.download_button("Download JSON", data=json_text, file_name=json_file)
   c2.download_button("Download Markdown", data=md_text, file_name=md_file)

if st.button("Save to outputs/"):
        out_dir = Path("outputs")
        out_dir.mkdir(parents=True, exist_ok=True)

        (out_dir / json_file).write_text(json_text, encoding="utf-8")
        (out_dir / md_file).write_text(md_text, encoding="utf-8")

        st.success(f"Saved outputs/{json_file} and outputs/{md_file}")  