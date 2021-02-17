# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pytorch_lightning import Trainer

from flash.core.data import download_data
from flash.text import SummarizationData, SummarizationTask

# 1. Download the data
download_data("https://pl-flash-data.s3.amazonaws.com/xsum.zip", "data/")

# 2. Load the model from a checkpoint
model = SummarizationTask.load_from_checkpoint("https://flash-weights.s3.amazonaws.com/summarization_model_xsum.pt")

# 2a. Summarize an article!
predictions = model.predict([
    """
    Camilla bought a box of mangoes with a Brixton Â£10 note, introduced last year to try to keep the money of local
    people within the community.The couple were surrounded by shoppers as they walked along Electric Avenue.
    They came to Brixton to see work which has started to revitalise the borough.
    It was Charles' first visit to the area since 1996, when he was accompanied by the former
    South African president Nelson Mandela.Greengrocer Derek Chong, who has run a stall on Electric Avenue
    for 20 years, said Camilla had been ""nice and pleasant"" when she purchased the fruit.
    ""She asked me what was nice, what would I recommend, and I said we've got some nice mangoes.
    She asked me were they ripe and I said yes - they're from the Dominican Republic.""
    Mr Chong is one of 170 local retailers who accept the Brixton Pound.
    Customers exchange traditional pound coins for Brixton Pounds and then spend them at the market
    or in participating shops.
    During the visit, Prince Charles spent time talking to youth worker Marcus West, who works with children
    nearby on an estate off Coldharbour Lane. Mr West said:
    ""He's on the level, really down-to-earth. They were very cheery. The prince is a lovely man.""
    He added: ""I told him I was working with young kids and he said, 'Keep up all the good work.'""
    Prince Charles also visited the Railway Hotel, at the invitation of his charity The Prince's Regeneration Trust.
    The trust hopes to restore and refurbish the building,
    where once Jimi Hendrix and The Clash played, as a new community and business centre."
    """
])
print(predictions)

# 2b. Or generate summaries from a sheet file!
datamodule = SummarizationData.from_file(
    predict_file="data/xsum/predict.csv",
    input="input",
)
predictions = Trainer().predict(model, datamodule=datamodule)
print(predictions)
