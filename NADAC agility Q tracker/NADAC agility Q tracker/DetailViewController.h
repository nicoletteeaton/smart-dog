//
//  DetailViewController.h
//  NADAC agility Q tracker
//
//  Created by Nicolette Eaton on 2/26/13.
//  Copyright (c) 2013 Nicolette Eaton. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DetailViewController : UIViewController <UISplitViewControllerDelegate>

@property (strong, nonatomic) id detailItem;

@property (weak, nonatomic) IBOutlet UILabel *detailDescriptionLabel;
@end
