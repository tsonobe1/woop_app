<template>
  <div>
    <!-- Split | Left Side "form"| Right Side "TIps" | -->
    <div id="css-grid">
      <!----------------------------------------------------------------------->
      <!--                       Left Side "form"                         -->
      <!----------------------------------------------------------------------->
      <v-container fluid id="form-area">
        <div id="line">
          <!-- Label -->
          <v-row>
            <v-col cols="10">
              <h2 class="message-title">Lets preparations for not give up.</h2>
            </v-col>
            <v-col>
              <v-btn small color="gray" @click="editWorry()">OK!</v-btn>
            </v-col>
          </v-row>

          <!----------------------------------------------------------------------->
          <!--            Obstacle & Countermeasure.                 -->
          <!----------------------------------------------------------------------->
          <h3 class="category-title">Obstacle & Countermeasure.</h3>
          <transition-group name="form" tag="div">
            <div
              v-for="(worries, worries_index) in WorryData.worries"
              :key="worries_index"
            >
              <!-- If it's two or more Worry Model forms, show ✘, and label and hint is hide of Worry. Idea Model form. -->
              <template v-if="worries_index >= 1">
                <v-row>
                  <v-col cols="11" md="11">
                    <v-textarea
                      rows="1"
                      auto-grow
                      v-model="worries.worry"
                    ></v-textarea>
                  </v-col>
                  <v-col cols="1">
                    <v-btn
                      @click="
                        deleteWorryIdeaForm(worries.worry_id, worries_index)
                      "
                      text
                      depressed
                      height="55"
                      color="error"
                    >
                      ✘
                    </v-btn>
                  </v-col>
                </v-row>

                <!-- Idea Model Form -->
                <transition-group name="form" tag="div">
                  <div
                    v-for="(ideas, ideas_index) in worries.ideas"
                    :key="ideas_index"
                  >
                    <v-row justify="end">
                      <v-col cols="2"></v-col>
                      <!--The second and subsequent Idea model forms belonging to the Worry model form will not be labeled or named. -->
                      <template v-if="ideas_index >= 1">
                        <v-col cols="9">
                          <v-textarea
                            rows="1"
                            auto-grow
                            v-model="ideas.idea"
                          ></v-textarea>
                        </v-col>

                        <v-col cols="1">
                          <v-btn
                            @click="
                              deleteIdeaForm(
                                worries.worry_id,
                                ideas.idea_id,
                                worries_index,
                                ideas_index
                              )
                            "
                            text
                            depressed
                            height="55"
                            color="error"
                          >
                            ✘
                          </v-btn>
                        </v-col>
                      </template>

                      <!-- First Idea Model form -->
                      <template v-else>
                        <v-col cols="9">
                          <v-textarea rows="1" auto-grow v-model="ideas.idea">
                          </v-textarea>
                        </v-col>
                        <v-col cols="1"> </v-col>
                      </template>
                    </v-row>
                  </div>
                </transition-group>
              </template>
              <!-- This is the end of the Worry Model form after 2. -->

              <!-- First Worry Model form -->
              <template v-else>
                <v-row>
                  <v-col cols="12">
                    <v-textarea
                      name="障壁"
                      label="Obstacle"
                      hint=""
                      rows="1"
                      auto-grow
                      v-model="worries.worry"
                    ></v-textarea>
                  </v-col>
                </v-row>

                <!-- Idea Model Form -->
                <transition-group name="form" tag="div">
                  <div
                    v-for="(ideas, ideas_index) in worries.ideas"
                    :key="ideas_index"
                  >
                    <v-row justify="end">
                      <v-col cols="2"></v-col>

                      <!-- If it's two or more Idea Model forms, show ✘, and label and hint is hide. -->
                      <template v-if="ideas_index >= 1">
                        <v-col cols="9">
                          <v-textarea rows="1" auto-grow v-model="ideas.idea">
                          </v-textarea>
                        </v-col>
                        <v-col cols="1">
                          <v-btn
                            @click="
                              deleteIdeaForm(
                                worries.worry_id,
                                ideas.idea_id,
                                worries_index,
                                ideas_index
                              )
                            "
                            text
                            depressed
                            height="55"
                            color="error"
                          >
                            ✘
                          </v-btn>
                        </v-col>
                      </template>
                      <!-- This is the end of the Idea Model form after 2.  -->

                      <!-- First Idea Model form -->
                      <template v-else>
                        <v-col>
                          <v-textarea
                            name="解決策"
                            label="Countermeasure."
                            hint=""
                            rows="1"
                            auto-grow
                            v-model="ideas.idea"
                          ></v-textarea></v-col
                      ></template>
                      <!-- This is the end of the First Idea Model form. -->
                    </v-row>
                  </div>
                </transition-group>
              </template>

              <v-row justify="end">
                <v-col cols="1">
                  <v-btn depressed small @click="addIdeaForm(worries_index)">
                    ＋
                  </v-btn>
                </v-col>
              </v-row>
            </div>
          </transition-group>

          <v-row>
            <v-col>
              <v-btn @click="addWorryIdeaForm" text depressed>＋</v-btn>
            </v-col>
          </v-row>

          <!----------------------------------------------------------------------->
          <!--                          Reference                               -->
          <!----------------------------------------------------------------------->
          <!--   <v&#45;form v&#45;model="valid"> -->
          <!--     <h3 class="category&#45;title">References</h3> -->
          <!--     <transition&#45;group name="form" tag="div"> -->
          <!--       <div -->
          <!--         v&#45;for="(references, ref_index) in refList" -->
          <!--         v&#45;bind:key="ref_index" -->
          <!--       > -->
          <!--         <!&#45;&#45; First Referenec Model form &#45;&#45;> -->
          <!--         <template v&#45;if="ref_index >= 1"> -->
          <!--           <v&#45;row> -->
          <!--             <v&#45;col cols="6"> -->
          <!--               <v&#45;text&#45;field v&#45;model="references.reference_name"> -->
          <!--               </v&#45;text&#45;field> -->
          <!--             </v&#45;col> -->
          <!--             <v&#45;col cols="6"> -->
          <!--               <v&#45;text&#45;field v&#45;model="references.reference_source"> -->
          <!--               </v&#45;text&#45;field> -->
          <!--             </v&#45;col> -->
          <!--           </v&#45;row> -->
          <!--  -->
          <!--           <v&#45;row> -->
          <!--             <v&#45;col cols="11"> -->
          <!--               <v&#45;text&#45;field v&#45;model="references.reference_use"> -->
          <!--               </v&#45;text&#45;field> -->
          <!--             </v&#45;col> -->
          <!--             <v&#45;col cols="1"> -->
          <!--               <v&#45;btn -->
          <!--                 @click="deleteRefernceForm(ref_index)" -->
          <!--                 color="error" -->
          <!--                 text -->
          <!--               > -->
          <!--                 ✘ -->
          <!--               </v&#45;btn> -->
          <!--             </v&#45;col> -->
          <!--           </v&#45;row> -->
          <!--         </template> -->
          <!--  -->
          <!--         <!&#45;&#45; after second  &#45;&#45;> -->
          <!--         <template v&#45;else> -->
          <!--           <v&#45;row> -->
          <!--             <v&#45;col cols="6"> -->
          <!--               <v&#45;text&#45;field -->
          <!--                 label="Name" -->
          <!--                 hint="" -->
          <!--                 v&#45;model="references.reference_name" -->
          <!--               ></v&#45;text&#45;field> -->
          <!--             </v&#45;col> -->
          <!--             <v&#45;col cols="6"> -->
          <!--               <v&#45;text&#45;field -->
          <!--                 label="URL" -->
          <!--                 hint="" -->
          <!--                 v&#45;model="references.reference_source" -->
          <!--               ></v&#45;text&#45;field> -->
          <!--             </v&#45;col> -->
          <!--           </v&#45;row> -->
          <!--  -->
          <!--           <v&#45;row> -->
          <!--             <v&#45;col cols="12"> -->
          <!--               <v&#45;text&#45;field -->
          <!--                 label="Use" -->
          <!--                 hint="" -->
          <!--                 v&#45;model="references.reference_use" -->
          <!--               ></v&#45;text&#45;field> -->
          <!--             </v&#45;col> -->
          <!--           </v&#45;row> -->
          <!--         </template> -->
          <!--       </div> -->
          <!--     </transition&#45;group> -->
          <!--  -->
          <!--     <v&#45;row justify="end"> -->
          <!--       <v&#45;col cols="1"> -->
          <!--         <v&#45;btn @click="addReferenceForm" depressed small> -->
          <!--           + -->
          <!--         </v&#45;btn> -->
          <!--       </v&#45;col> -->
          <!--     </v&#45;row> -->
          <!--     <v&#45;btn outlined @click="counterMeasureAllRegister">登録！</v&#45;btn> -->
          <!--   </v&#45;form> -->
        </div>
      </v-container>

      <!----------------------------------------------------------------------->
      <!--                       Right Side "form"                        -->
      <!----------------------------------------------------------------------->
      <v-container fluid id="tips-area">
        <h1>Tips</h1>
      </v-container>
    </div>
  </div>
</template>

<script>
import api from "@/services/api.js";

export default {
  name: "Goal",
  props: ["Worries", "OriginalWorries"],

  data: function () {
    return {
      valid: "",
      worryList: [{ worry: "", ideaList: [{ idea: "" }] }],
      parentWorryId: "",
      refList: [
        { reference_name: "", reference_use: "", reference_source: "" }
      ],

      WorryData: this.Worries,
      OriginalWorryData: this.OriginalWorries
    };
  },

  methods: {
    //  ------------------------------------------------------------
    //                   Form  Increase
    //  ------------------------------------------------------------
    addWorryIdeaForm: function () {
      const form = { worry: "", ideas: [{ idea: "" }] };
      this.Worries.worries.push(form);
    },
    addIdeaForm: function (worries_id) {
      const form = { idea: "" };
      this.Worries.worries[worries_id].ideas.push(form);
    },
    addReferenceForm: function () {
      const form = {
        reference_name: "",
        reference_use: "",
        reference_source: ""
      };
      this.refList.push(form);
    },

    //  ------------------------------------------------------------
    //                   Form Delete
    //  ------------------------------------------------------------
    deleteWorryIdeaForm(worry_id, index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (worry_id == null) {
        vm.WorryData.worries.splice(index, 1);
      } else {
        api
          .delete(`goals/${goalid}/worries/${worry_id}/`)
          .then(response => console.log(response))
          .catch(error => console.log(error));
        vm.WorryData.worries.splice(index, 1);
        vm.OriginalWorryData.worries.worries.splice(index, 1);
      }
    },

    deleteIdeaForm(worry_id, idea_id, worries_index, ideas_index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (idea_id == null) {
        vm.WorryData.worries[worries_index].ideas.splice(ideas_index, 1);
      } else {
        api
          .delete(`goals/${goalid}/worries/${worry_id}/ideas/${idea_id}/`)
          .then(response => console.log(response))
          .catch(error => console.log(error));
        vm.WorryData.worries[worries_index].ideas.splice(ideas_index, 1);
        vm.OriginalWorryData.worries.worries[worries_index].ideas.splice(
          ideas_index,
          1
        );
      }
    },
    // deleteRefernceForm: function (index) {
    //   this.refList.splice(index, 1);
    //   console.log(this.refList);
    // },
    endEdit: function () {
      this.$emit("close");
    },

    editWorry: function () {
      const vm = this;
      // Stores the object whose content has changed.
      let ChangeData = [];
      let NewData = [];
      let postPromises = []; // post datas
      let editPromises = []; // patch datas
      let NewIdeaData = [];
      let ChangeIdeaData = [];
      let postIdeaPromises = [];
      let editIdeaPromises = [];

      let goalId = vm.$route.params.id;

      Array.from(vm.WorryData.worries).forEach((worry, index) => {
        // For compute to difference by `OriginalMotives`.
        let originalMo = vm.OriginalWorryData.worries.worries[index];
        let ideaList = [];

        // If existence new `Worry`
        if (!worry.worry_id) {
          // add new `ideas`
          ideaList = worry.ideas.map(idea => {
            return { idea: idea.idea };
          });
          console.log(ideaList)
          NewData.push({
            worry: worry.worry,
            ideas: ideaList // ideaList = { idea: '', worry: 1}, { idea: '', worry:1}, ......
          });
        }

        // edit Worry
        else if (worry.worry !== originalMo.worry) {
          ChangeData.push({
            worry_id: worry.worry_id,
            worry: worry.worry
          });
          // and idea diff
          if (worry.ideas !== originalMo.ideas) {
            Array.from(worry.ideas).forEach((idea, index) => {
              let original = originalMo.ideas[index];
              let currentWorryId = worry.worry_id;
              if (!idea.idea_id) {
                // idea = new input data, original = original
                NewIdeaData.push({
                  worry: worry.worry_id,
                  idea: idea.idea
                });
              } else if (idea.idea !== original.idea) {
                ChangeIdeaData.push({
                  idea_id: original.idea_id,
                  idea: idea.idea,
                  worry: original.worry
                });
              }
            });
          }
        }
        // edit Idea ( Worry is still the same. )
        else if (worry.ideas !== originalMo.ideas) {
          Array.from(worry.ideas).forEach((idea, index) => {
            let original = originalMo.ideas[index];
            let currentWorryId = worry.worry_id;
            if (!idea.idea_id) {
              // idea = new input data, original = original
              NewIdeaData.push({
                worry: worry.worry_id,
                idea: idea.idea
              });
            } else if (idea.idea !== original.idea) {
              ChangeIdeaData.push({
                idea_id: original.idea_id,
                idea: idea.idea,
                worry: original.worry
              });
            }
          });
        }
      });

      //create post datas and axios.all
      NewData.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/worries/`,
          data: { worry: item.worry, ideas: item.ideas, goal: goalId },
          useCredentails: true
        });
        postPromises.push(newPostPromise);
        console.log(item.ideas)
        console.log(newPostPromise)
      });
      // idea
      NewIdeaData.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/worries/${item.worry}/ideas/`,
          data: { idea: item.idea, worry: item.worry },
          useCredentails: true
        });
        postIdeaPromises.push(newPostPromise);
      });

      // create patch datas
      ChangeData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/worries/${item.worry_id}/`,
          data: {
            worry: item.worry
          },
          useCredentails: true
        });
        editPromises.push(newPromise);
      });
      // idea
      ChangeIdeaData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/worries/${item.worry}/ideas/${item.idea_id}/`,
          data: {
            idea: item.idea
          },
          useCredentails: true
        });
        editIdeaPromises.push(newPromise);
      });

      // post
      Promise.all(postPromises).then(responses => {
        responses.forEach(res => {
          vm.OriginalWorryData.worries.worries.push(res.data);
          vm.$set(
            vm.WorryData,
            "worries",
            // Deep Copy
            JSON.parse(JSON.stringify(vm.OriginalWorryData.worries.worries))
          );
        });
      });

      Promise.all(postIdeaPromises).then(responses => {
        responses.forEach(res => {
          let postIdea = res.data;
          // Identifying the Parent Object.
          if (
            vm.OriginalWorryData.worries.worries.find(
              item => item.worry_id == postIdea.worry
            )
          ) {
            vm.OriginalWorryData.worries.worries
              .find(item => item.worry_id == postIdea.worry)
              .ideas.push(postIdea);

            vm.$set(
              vm.WorryData,
              "worries",
              // Deep Copy
              JSON.parse(JSON.stringify(vm.OriginalWorryData.worries.worries))
            );
          }
        });
      });

      // patch
      Promise.all(editPromises).then(responses => {
        responses.forEach(res => {
          let currentId = res.data.worry_id;
          // Find the object to be changed by `OriginalMotive`.
          // superscription motive.
          if (
            vm.OriginalWorryData.worries.worries.find(
              item => item.worry_id == currentId
            )
          ) {
            vm.OriginalWorryData.worries.worries.find(
              item => item.worry_id == currentId
            ).worry = res.data.worry;

            vm.$set(
              vm.WorryData,
              "worries",
              // Deep Copy
              JSON.parse(JSON.stringify(vm.OriginalWorryData.worries.worries))
            );
          }
        });
      });

      Promise.all(editIdeaPromises).then(responses => {
        responses.forEach(res => {
          let postIdea = res.data;
          // Identifying the Parent Object.
          if (
            vm.OriginalWorryData.worries.worries.find(
              item => item.worry_id == postIdea.worry
            )
          ) {
            vm.OriginalWorryData.worries.worries
              .find(item => item.worry_id == postIdea.worry)
              .ideas.find(i => i.idea_id == postIdea.idea_id).idea =
              postIdea.idea;

            vm.$set(
              vm.WorryData,
              "worries",
              // Deep Copy
              JSON.parse(JSON.stringify(vm.OriginalWorryData.worries.worries))
            );
          }
        });
      });

      vm.$emit("close");
    }
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  background-color: #f0f0f0;
}

#form-area {
  grid-area: form;
}
#tips-area {
  grid-area: tips;
}

@media all and (max-width: 100000px) {
  #css-grid {
    grid-template-columns: 55% 45%;
    grid-template-areas: "form tips";
    padding: 0px 17%;
  }
}

@media all and (max-width: 1264px) {
  #css-grid {
    grid-template-columns: 100%;
    grid-template-areas:
      "form"
      "tips";
    padding: 0px 13%;
  }
}

@media all and (max-width: 960px) {
  #css-grid {
    padding: 0px 5%;
  }
}

/*   ------------------------------------------------------------
                          Transition
 ------------------------------------------------------------*/
.countermeasure-enter-active,
.countermeasure-leave-active {
  transition: opacity 0.3s;
}
.countermeasure-enter,
.countermeasure-leave-to {
  opacity: 0;
}

/* add(delete) form */
.form-enter-active {
  animation: fadeInUp 0.3s;
  transition: opacity 0.3s;
}
.form-leave-active {
  animation: fadeInUp 0.3s reverse;
  transition: opacity 0.3s;
}
.form-enter,
.form-leave-to {
  opacity: 0;
}

@keyframes fadeInUp {
  0% {
    transform: translateX(20px);
    opacity: 0;
  }
  60% {
    opacity: 0.3;
  }
  100% {
    transform: translateX(0px);
    opacity: 1;
  }
}

/*   ------------------------------------------------------------
                            Font Desiign
------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 34px;
  line-height: 40px;
  color: #4465c0;
}

.category-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 40px;
  color: #3c3d3d;
}
</style>
