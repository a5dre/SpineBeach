game = {
  "story": "Spine Beach",
  "startnode": "1",
  "passages": [
    {
      "name": "game1",
      "tags": "",
      "pid": "1",
      "text": "Your brother, Sam, offers you a sip from his flask, he doesn't seem to care what's in it, but he's been drinking from it all morning. \"Care for a sip?\" he asks.\n\n[[\"Sure, thanks\"->game2]]\n[[\"I'm Alright\"->game2]]",
      "links": [
        {
          "original": "[[\"Sure, thanks\"->game2]]",
          "label": "\"Sure, thanks\"",
          "newPassage": "game2",
          "pid": "2",
          "selection": "1"
        },
        {
          "original": "[[\"I'm Alright\"->game2]]",
          "label": "\"I'm Alright\"",
          "newPassage": "game2",
          "pid": "2",
          "selection": "2"
        }
      ],
      "cleanText": "Your brother, Sam, offers you a sip from his flask, he doesn't seem to care what's in it, but he's been drinking from it all morning. \"Care for a sip?\" he asks."
    },
    {
      "name": "game2",
      "tags": "",
      "pid": "2",
      "text": "You're about 10 minutes from the shore. You close your eyes and decide to get some rest.\n\n[[Sleep->game3]]",
      "links": [
        {
          "original": "[[Sleep->game3]]",
          "label": "Sleep",
          "newPassage": "game3",
          "pid": "3",
          "selection": "1"
        }
      ],
      "cleanText": "You're about 10 minutes from the shore. You close your eyes and decide to get some rest."
    },
    {
      "name": "game3",
      "tags": "",
      "pid": "3",
      "text": "A deafining chrash awakes you. All of a sudden, bullets and small explosions can be heard just 50 yards from where your boat landed. You watch Sam get up as he leads the rest of the men from your boat to the shore. \n\n[[Catch up to him->game4]]\n[[Stay in the back->game5]]",
      "links": [
        {
          "original": "[[Catch up to him->game4]]",
          "label": "Catch up to him",
          "newPassage": "game4",
          "pid": "4",
          "selection": "1"
        },
        {
          "original": "[[Stay in the back->game5]]",
          "label": "Stay in the back",
          "newPassage": "game5",
          "pid": "5",
          "selection": "2"
        }
      ],
      "cleanText": "A deafining chrash awakes you. All of a sudden, bullets and small explosions can be heard just 50 yards from where your boat landed. You watch Sam get up as he leads the rest of the men from your boat to the shore."
    },
    {
      "name": "game4",
      "tags": "",
      "pid": "4",
      "text": "Instantly, you feel the ground shaking beneath you. You see fortresses in the distance filled with men of the opposing powers. \"Take Cover!\" Sam yells. \n\n[[Follow Sam to cover->game6]]\n[[Split up and find the best cover for yourself->game7]]",
      "links": [
        {
          "original": "[[Follow Sam to cover->game6]]",
          "label": "Follow Sam to cover",
          "newPassage": "game6",
          "pid": "6",
          "selection": "1"
        },
        {
          "original": "[[Split up and find the best cover for yourself->game7]]",
          "label": "Split up and find the best cover for yourself",
          "newPassage": "game7",
          "pid": "7",
          "selection": "2"
        }
      ],
      "cleanText": "Instantly, you feel the ground shaking beneath you. You see fortresses in the distance filled with men of the opposing powers. \"Take Cover!\" Sam yells."
    },
    {
      "name": "game5",
      "tags": "",
      "pid": "5",
      "text": "Instantly, you feel the ground is shaking beneath you. You see fortresses in the distance filled with men of the opposing powers. You hear Sam yell but you can't make out what he's saying. Suddenly, everyone you know begins to scatter.\n\n[[Try to find Sam->game6]]\n[[Try to get to safety->game7]]",
      "links": [
        {
          "original": "[[Try to find Sam->game6]]",
          "label": "Try to find Sam",
          "newPassage": "game6",
          "pid": "6",
          "selection": "1"
        },
        {
          "original": "[[Try to get to safety->game7]]",
          "label": "Try to get to safety",
          "newPassage": "game7",
          "pid": "7",
          "selection": "2"
        }
      ],
      "cleanText": "Instantly, you feel the ground is shaking beneath you. You see fortresses in the distance filled with men of the opposing powers. You hear Sam yell but you can't make out what he's saying. Suddenly, everyone you know begins to scatter."
    },
    {
      "name": "game6",
      "tags": "",
      "pid": "6",
      "text": "Sam has already vanished, along with half of the group you arrived with. You have to think quickly. You see fellow soldiers about 20 meters to your left laying on their stomachs beneath a hill. You also see a bush to your right, surrounded by barbed wire. \n\n[[Move to the bush->game7]]\n[[Move to the hill->game12]]\n[[Move forwards in hopes of finding Sam->game13death]]",
      "links": [
        {
          "original": "[[Move to the bush->game7]]",
          "label": "Move to the bush",
          "newPassage": "game7",
          "pid": "7",
          "selection": "1"
        },
        {
          "original": "[[Move to the hill->game12]]",
          "label": "Move to the hill",
          "newPassage": "game12",
          "pid": "12",
          "selection": "2"
        },
        {
          "original": "[[Move forwards in hopes of finding Sam->game13death]]",
          "label": "Move forwards in hopes of finding Sam",
          "newPassage": "game13death",
          "pid": "13",
          "selection": "3"
        }
      ],
      "cleanText": "Sam has already vanished, along with half of the group you arrived with. You have to think quickly. You see fellow soldiers about 20 meters to your left laying on their stomachs beneath a hill. You also see a bush to your right, surrounded by barbed wire."
    },
    {
      "name": "game7",
      "tags": "",
      "pid": "7",
      "text": "You quickly run to a nearby bush covered with a layer of barbed wire. You can't see Sam anywhere, just pure chaos. You need to get some eyes on the turrets and infantry that are so heavily surpressing you. You see a boulder 20 meters to your left with a familiar soldier taking cover behind it.\n\n[[Raise your head above the bush->game8]]\n[[Move to the boulder->game9]]",
      "links": [
        {
          "original": "[[Raise your head above the bush->game8]]",
          "label": "Raise your head above the bush",
          "newPassage": "game8",
          "pid": "8",
          "selection": "1"
        },
        {
          "original": "[[Move to the boulder->game9]]",
          "label": "Move to the boulder",
          "newPassage": "game9",
          "pid": "9",
          "selection": "2"
        }
      ],
      "cleanText": "You quickly run to a nearby bush covered with a layer of barbed wire. You can't see Sam anywhere, just pure chaos. You need to get some eyes on the turrets and infantry that are so heavily surpressing you. You see a boulder 20 meters to your left with a familiar soldier taking cover behind it."
    },
    {
      "name": "game8",
      "tags": "",
      "pid": "8",
      "text": "It's hard to get a good view, but you see lots of smoke, fire, and can smell burning rubber. You also see a wooden tower with a man on top and assume he is a long-ranged assassin. \n\n[[Aim at the man and fire->game10]]\n[[Keep moving forward to find Sam->game11]]",
      "links": [
        {
          "original": "[[Aim at the man and fire->game10]]",
          "label": "Aim at the man and fire",
          "newPassage": "game10",
          "pid": "10",
          "selection": "1"
        },
        {
          "original": "[[Keep moving forward to find Sam->game11]]",
          "label": "Keep moving forward to find Sam",
          "newPassage": "game11",
          "pid": "11",
          "selection": "2"
        }
      ],
      "cleanText": "It's hard to get a good view, but you see lots of smoke, fire, and can smell burning rubber. You also see a wooden tower with a man on top and assume he is a long-ranged assassin."
    },
    {
      "name": "game9",
      "tags": "",
      "pid": "9",
      "text": "As you get to the boulder, the man you are with begins to cry. He hands you a photo of his wife and asks you to find her when you go home. You take it, but know you can't stay behind here forever. \n\n[[Keep moving forward to find Sam->game11]]",
      "links": [
        {
          "original": "[[Keep moving forward to find Sam->game11]]",
          "label": "Keep moving forward to find Sam",
          "newPassage": "game11",
          "pid": "11",
          "selection": "1"
        }
      ],
      "cleanText": "As you get to the boulder, the man you are with begins to cry. He hands you a photo of his wife and asks you to find her when you go home. You take it, but know you can't stay behind here forever."
    },
    {
      "name": "game10",
      "tags": "",
      "pid": "10",
      "text": "You take three shots. The first of which was missed and alerts him to your position. The second shot also misses, and allows him to see you. Fortunately, you hit the third shot. The man's body collapses and he no longer poses a threat. A small victory is nice, however the battle is not over. You need to find Sam. You see a group soldiers ahead of you laying beneath a hill.  \n\n[[Move forward to the Hill->game12]]\n[[Keep moving forward to find Sam->game11]]",
      "links": [
        {
          "original": "[[Move forward to the Hill->game12]]",
          "label": "Move forward to the Hill",
          "newPassage": "game12",
          "pid": "12",
          "selection": "1"
        },
        {
          "original": "[[Keep moving forward to find Sam->game11]]",
          "label": "Keep moving forward to find Sam",
          "newPassage": "game11",
          "pid": "11",
          "selection": "2"
        }
      ],
      "cleanText": "You take three shots. The first of which was missed and alerts him to your position. The second shot also misses, and allows him to see you. Fortunately, you hit the third shot. The man's body collapses and he no longer poses a threat. A small victory is nice, however the battle is not over. You need to find Sam. You see a group soldiers ahead of you laying beneath a hill."
    },
    {
      "name": "game11",
      "tags": "",
      "pid": "11",
      "text": "A valley of sands and shrubs has been formed in the war torn terrain. Crouching, you walk along the bottom of the valley. Passing fallen soldiers, some of them face up and others lie down, none of them moving. \n\n[[Keep moving forward->game14]]\n[[Check bodies to see if Sam is lying face down in the valley->game15death]]",
      "links": [
        {
          "original": "[[Keep moving forward->game14]]",
          "label": "Keep moving forward",
          "newPassage": "game14",
          "pid": "14",
          "selection": "1"
        },
        {
          "original": "[[Check bodies to see if Sam is lying face down in the valley->game15death]]",
          "label": "Check bodies to see if Sam is lying face down in the valley",
          "newPassage": "game15death",
          "pid": "15",
          "selection": "2"
        }
      ],
      "cleanText": "A valley of sands and shrubs has been formed in the war torn terrain. Crouching, you walk along the bottom of the valley. Passing fallen soldiers, some of them face up and others lie down, none of them moving."
    },
    {
      "name": "game12",
      "tags": "",
      "pid": "12",
      "text": "You meet with the group of men at the bottom of the hill, all too scared to move. Slightly exposed, you begin to get a bad feeling.\n\n[[Stay at the hill->game13death]]\n[[Keep moving forward to find Sam->game11]]",
      "links": [
        {
          "original": "[[Stay at the hill->game13death]]",
          "label": "Stay at the hill",
          "newPassage": "game13death",
          "pid": "13",
          "selection": "1"
        },
        {
          "original": "[[Keep moving forward to find Sam->game11]]",
          "label": "Keep moving forward to find Sam",
          "newPassage": "game11",
          "pid": "11",
          "selection": "2"
        }
      ],
      "cleanText": "You meet with the group of men at the bottom of the hill, all too scared to move. Slightly exposed, you begin to get a bad feeling."
    },
    {
      "name": "game13death",
      "tags": "",
      "pid": "13",
      "text": "The sharp pain of a bullet passes through your chest. Your knees begin to wobble as the sand beneath you turns red. The world goes dark.\n\nYou died.",
      "links": [],
      "cleanText": "The sharp pain of a bullet passes through your chest. Your knees begin to wobble as the sand beneath you turns red. The world goes dark.\n\nYou died."
    },
    {
      "name": "game14",
      "tags": "",
      "pid": "14",
      "text": "You look back and the beach is now quite far behind you. The only thing you can think of is surviving to find Sam. Up ahead you see a group of soldiers taking cover behind a flipped caravan. \n\n[[Catch up to them->game16]]\n[[Move past them->game17]]",
      "links": [
        {
          "original": "[[Catch up to them->game16]]",
          "label": "Catch up to them",
          "newPassage": "game16",
          "pid": "16",
          "selection": "1"
        },
        {
          "original": "[[Move past them->game17]]",
          "label": "Move past them",
          "newPassage": "game17",
          "pid": "17",
          "selection": "2"
        }
      ],
      "cleanText": "You look back and the beach is now quite far behind you. The only thing you can think of is surviving to find Sam. Up ahead you see a group of soldiers taking cover behind a flipped caravan."
    },
    {
      "name": "game15death",
      "tags": "",
      "pid": "15",
      "text": "You begin to spend too much time in the valley, over-exposed. The sharp pain of a bullet passes through your chest. Your knees begin to wobble as the sand beneath you turns red. The world goes dark.\n\nYou died.",
      "links": [],
      "cleanText": "You begin to spend too much time in the valley, over-exposed. The sharp pain of a bullet passes through your chest. Your knees begin to wobble as the sand beneath you turns red. The world goes dark.\n\nYou died."
    },
    {
      "name": "game16",
      "tags": "",
      "pid": "16",
      "text": "\"Sam!\" you shout, in hopes he is with them. The soldiers turn around and you can't see Sam's face anywhere. The shout brought attention to you. You see a trail of bullet marks entering the sand behind you as you sprint full speed, tripping and stumbling, to the group of soldiers. They help you up, but Sam is not present. \n\n[[Ask for their help in finding Sam->game18]]\n[[Keep moving forward by yourself->game17]]",
      "links": [
        {
          "original": "[[Ask for their help in finding Sam->game18]]",
          "label": "Ask for their help in finding Sam",
          "newPassage": "game18",
          "pid": "18",
          "selection": "1"
        },
        {
          "original": "[[Keep moving forward by yourself->game17]]",
          "label": "Keep moving forward by yourself",
          "newPassage": "game17",
          "pid": "17",
          "selection": "2"
        }
      ],
      "cleanText": "\"Sam!\" you shout, in hopes he is with them. The soldiers turn around and you can't see Sam's face anywhere. The shout brought attention to you. You see a trail of bullet marks entering the sand behind you as you sprint full speed, tripping and stumbling, to the group of soldiers. They help you up, but Sam is not present."
    },
    {
      "name": "game17",
      "tags": "",
      "pid": "17",
      "text": "You see a few fallen trees, a ditch, and pile of sandbags with soldiers behind it. You think sam could be at any of these three places. \n[[Proceed to fallen tree trunks->game19]]\n[[Proceed to ditch->game20death]]\n[[Proceed to cover behind sandbags->game21]]",
      "links": [
        {
          "original": "[[Proceed to fallen tree trunks->game19]]",
          "label": "Proceed to fallen tree trunks",
          "newPassage": "game19",
          "pid": "19",
          "selection": "1"
        },
        {
          "original": "[[Proceed to ditch->game20death]]",
          "label": "Proceed to ditch",
          "newPassage": "game20death",
          "pid": "20",
          "selection": "2"
        },
        {
          "original": "[[Proceed to cover behind sandbags->game21]]",
          "label": "Proceed to cover behind sandbags",
          "newPassage": "game21",
          "pid": "21",
          "selection": "3"
        }
      ],
      "cleanText": "You see a few fallen trees, a ditch, and pile of sandbags with soldiers behind it. You think sam could be at any of these three places."
    },
    {
      "name": "game18",
      "tags": "",
      "pid": "18",
      "text": "As you describe Sam to the group, one man believes to have seen him up ahead, laying beneath a fallen tree trunk. He knows you must find him, and gives you some water. You thank him and keep moving forward.\n\n[[Slowly make your way to the fallen trunk in the distance->game19]]",
      "links": [
        {
          "original": "[[Slowly make your way to the fallen trunk in the distance->game19]]",
          "label": "Slowly make your way to the fallen trunk in the distance",
          "newPassage": "game19",
          "pid": "19",
          "selection": "1"
        }
      ],
      "cleanText": "As you describe Sam to the group, one man believes to have seen him up ahead, laying beneath a fallen tree trunk. He knows you must find him, and gives you some water. You thank him and keep moving forward."
    },
    {
      "name": "game19",
      "tags": "",
      "pid": "19",
      "text": "After 20 minutes of finding a safe route to the tree trunk, you finally begin to close in. As it becomes clear that Sam is laying beneath it, you begin to run. This is the first time you have smiled all day. However Sam is not responding. Perhaps he cannot hear you, or perhaps... \n\n[[Turn over his body->game22end]]",
      "links": [
        {
          "original": "[[Turn over his body->game22end]]",
          "label": "Turn over his body",
          "newPassage": "game22end",
          "pid": "22",
          "selection": "1"
        }
      ],
      "cleanText": "After 20 minutes of finding a safe route to the tree trunk, you finally begin to close in. As it becomes clear that Sam is laying beneath it, you begin to run. This is the first time you have smiled all day. However Sam is not responding. Perhaps he cannot hear you, or perhaps..."
    },
    {
      "name": "game20death",
      "tags": "",
      "pid": "20",
      "text": "When you arrive at the ditch, you jump down quickly to rest. You can't recognize any faces, or even any uniforms. Suddenly, you are yelled at in a different language. A sharp pain passes through your chest. Your knees begin to wobble as the sand beneath you turns red. The world goes dark.\n\nYou died.",
      "links": [],
      "cleanText": "When you arrive at the ditch, you jump down quickly to rest. You can't recognize any faces, or even any uniforms. Suddenly, you are yelled at in a different language. A sharp pain passes through your chest. Your knees begin to wobble as the sand beneath you turns red. The world goes dark.\n\nYou died."
    },
    {
      "name": "game21",
      "tags": "",
      "pid": "21",
      "text": "Arriving at the sandbags, the soldiers pull you down to their level to avoid being a target. You explain that you need to find your brother and they point you in the direction of the fallen tree trunk. \n\n[[Stay with the soldiers to get more information->game23death]]\n[[Move to the tree trunk->game19]]",
      "links": [
        {
          "original": "[[Stay with the soldiers to get more information->game23death]]",
          "label": "Stay with the soldiers to get more information",
          "newPassage": "game23death",
          "pid": "23",
          "selection": "1"
        },
        {
          "original": "[[Move to the tree trunk->game19]]",
          "label": "Move to the tree trunk",
          "newPassage": "game19",
          "pid": "19",
          "selection": "2"
        }
      ],
      "cleanText": "Arriving at the sandbags, the soldiers pull you down to their level to avoid being a target. You explain that you need to find your brother and they point you in the direction of the fallen tree trunk."
    },
    {
      "name": "game22end",
      "tags": "",
      "pid": "22",
      "text": "He coughs, blood lands on his clothes. As you hold him in your arms, you hear him begin to speak. You move your ear closer to his lips. \"Sometimes I still think I changed in ways that people I loved couldn't like or accept.\" He closes his eyes and you hug him. It is quiet, a different type of quiet. You look up and see soldiers yelling to one another. You hear \"ceasefire\". Just a bit too late. \n\nYou returned home safely, and alone.",
      "links": [],
      "cleanText": "He coughs, blood lands on his clothes. As you hold him in your arms, you hear him begin to speak. You move your ear closer to his lips. \"Sometimes I still think I changed in ways that people I loved couldn't like or accept.\" He closes his eyes and you hug him. It is quiet, a different type of quiet. You look up and see soldiers yelling to one another. You hear \"ceasefire\". Just a bit too late. \n\nYou returned home safely, and alone."
    },
    {
      "name": "game23death",
      "tags": "",
      "pid": "23",
      "text": "You listen to the soliders talk about their families and their own siblings. You care, but truly want to find Sam. Suddenly, the man next to you is hit in the head with an oval shaped rock that was thrown at the group. Unfortunately, it was not a rock but a grenade. Your body fills with heat as you feel your limbs come apart. \n\nYou died.",
      "links": [],
      "cleanText": "You listen to the soliders talk about their families and their own siblings. You care, but truly want to find Sam. Suddenly, the man next to you is hit in the head with an oval shaped rock that was thrown at the group. Unfortunately, it was not a rock but a grenade. Your body fills with heat as you feel your limbs come apart. \n\nYou died."
    }
  ]
}